from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.ycdoi.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

from datetime import datetime

@app.route('/')
def main():
    matjips = list(db.matjipprac2.find({},{"_id": False}))
    return render_template('main_page3.html', matjips=matjips)


@app.route('/detail')
def detail():
   return render_template('detail_page.html')

@app.route("/matjip", methods=["POST"])
def matjip_post():
    title_receive = request.form['title_give']
    place_receive = request.form['place_give']
    impre_receive = request.form['impre_give']
    url_receive = request.form['url_give']

    picture = request.files["picture_give"]

    # 확장자를 골라주는 코드 코드(뒤에서 부터 첫번째 점으로 나눠준다)
    extension = picture.filename.split('.')[-1]

    # 현재시간을 나타내주는 코드
    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')

    filename = f'picture-{mytime}'

    # static폴더에 저장해라
    save_to = f'static/{filename},{extension}'
    picture.save(save_to)

    # matjip_list = list(db.matjipprac.find({}, {'_id': False}))
    #
    # count = len(matip_list) + 1

    doc = {
        'title': title_receive,
        'place': place_receive,
        'url': url_receive,
        'impre': impre_receive,
        'picture': f'{filename},{extension}'

    }

    db.matjipprac2.insert_one(doc)

    return jsonify({'msg': '등록 완료 !'})
    return render_template("main_page3.html")




# @app.route('/listing', methods=['GET'])
# def listing():
#     matjips = list(db.matjipprac.find({},{'_id':False}))
#     return jsonify({'matjips':matjips})








if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)