from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb+srv://test:sparta@cluster0.kdwwh.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.test1

# JWT 토큰을 만들 때 필요한 비밀문자열입니다. 아무거나 입력해도 괜찮습니다.
# 이 문자열은 서버만 알고있기 때문에, 내 서버에서만 토큰을 인코딩(=만들기)/디코딩(=풀기) 할 수 있습니다.
SECRET_KEY = 'SPARTA'

# JWT 패키지를 사용합니다. (설치해야할 패키지 이름: PyJWT)
import jwt

# 토큰에 만료시간을 줘야하기 때문에, datetime 모듈도 사용합니다.
import datetime

# 회원가입 시엔, 비밀번호를 암호화하여 DB에 저장해두는 게 좋습니다.
# 그렇지 않으면, 개발자(=나)가 회원들의 비밀번호를 볼 수 있으니까요.^^;
import hashlib


#################################
##  HTML을 주는 부분             ##
#################################
@app.route('/')
def home():

    return render_template('index.html')

@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)

#################################
##  로그인을 위한 API            ##
#################################

# [회원가입 API]
@app.route('/sign_up/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    email_receive = request.form['email_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,
        "password": password_hash,
        "email": email_receive
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})

# [중복확인 API]
@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    # print(value_receive, type_receive, exists)
    return jsonify({'result': 'success', 'exists': exists})


# [로그인 API]
# id, pw를 받아서 맞춰보고, 토큰을 만들어 발급합니다.
@app.route('/api/login', methods=['POST'])
def api_login():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    # 회원가입 때와 같은 방법으로 pw를 암호화합니다.
    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()

    # id, 암호화된pw을 가지고 해당 유저를 찾습니다.
    result = db.users.find_one({'username': username_receive, 'password': pw_hash})

    # 찾으면 JWT 토큰을 만들어 발급합니다.
    if result is not None:
        # JWT 토큰에는, payload와 시크릿키가 필요합니다.
        # 시크릿키가 있어야 토큰을 디코딩(=풀기) 해서 payload 값을 볼 수 있습니다.
        # 아래에선 id와 exp를 담았습니다. 즉, JWT 토큰을 풀면 유저ID 값을 알 수 있습니다.
        # exp에는 만료시간을 넣어줍니다. 만료시간이 지나면, 시크릿키로 토큰을 풀 때 만료되었다고 에러가 납니다.
        payload = {
            'id': username_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60*60*24)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        # token을 줍니다.
        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


# [유저 정보 확인 API]
# 로그인된 유저만 call 할 수 있는 API입니다.
# 유효한 토큰을 줘야 올바른 결과를 얻어갈 수 있습니다.
# (그렇지 않으면 남의 장바구니라든가, 정보를 누구나 볼 수 있겠죠?)
@app.route('/main', methods=['GET'])
def api_valid():
    token_receive = request.cookies.get('mytoken')

    # try / catch 문?
    # try 아래를 실행했다가, 에러가 있으면 except 구분으로 가란 얘기입니다.

    try:
        # token을 시크릿키로 디코딩합니다.
        # 보실 수 있도록 payload를 print 해두었습니다. 우리가 로그인 시 넣은 그 payload와 같은 것이 나옵니다.
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        print(payload)
        # payload 안에 id가 들어있습니다. 이 id로 유저정보를 찾습니다.
        # 여기에선 그 예로 닉네임을 보내주겠습니다.
        userinfo = db.users.find_one({'id': payload['id']}, {'_id': 0})
        return render_template('main.html', user_info=userinfo)
    except jwt.ExpiredSignatureError:
        # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})

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
    today = datetime.datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')

    filename = f'picture-{mytime}'

    # static폴더에 저장해라
    save_to = f'static/{filename},{extension}'
    picture.save(save_to)

    doc = {
        'title': title_receive,
        'place': place_receive,
        'url': url_receive,
        'impre': impre_receive,
        'picture': f'{filename},{extension}'

    }

    db.matjipprac3.insert_one(doc)

    return jsonify({'msg': '등록 완료 !'})

@app.route('/listing', methods=['GET'])
def listing():
    matjips = list(db.matjipprac3.find({}, {'_id': False}))
    return jsonify({'matjips': matjips})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)