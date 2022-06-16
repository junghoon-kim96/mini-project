# 프로젝트명 : 너알맛
항해99 7기 C반 2팀 1주차 미니 프로젝트
>
##### <span style="color:royalblue"> - 친구,지인,모르는사람 할거 없이 내가 갔던 맛집을 공유하며 음식으로 교감을 쌓아보자 </span>

<깃헙주소>
https://github.com/junghoon-kim96/mini-project

<도메인주소>
http://54.180.94.64

---
#### 개발자 🙋🏻‍♂️ 🙋🏻‍♀️
김정훈[@junghoon-kim96](https://github.com/junghoon-kim96) / 팀장
- [x] 메인 페이지 담당(Feed)


한흥광
- [x] 작성 페이지 담당

 
이주현[@juhyunju](https://github.com/juhyunju)
- [x] 로그인 페이지 담당


김창규[@ck-kor] 
- [x] 회원가입 페이지 담당



---
### 프로젝트 화면
<입장 페이지>
![](https://user-images.githubusercontent.com/105117965/168012721-a7e1d900-7286-4fed-9f00-d8645c2c836d.png)

--- 
<로그인 페이지>
![](https://user-images.githubusercontent.com/105117965/168012930-3c41702b-2525-485a-9ac0-cfd3107e619f.png)

---
<회원가입 페이지>
![](https://user-images.githubusercontent.com/105117965/168013048-7502e1f4-f476-41df-8648-bd543b99b18e.png)

---
<메인 페이지>
![](https://user-images.githubusercontent.com/105117965/168019086-26a9bf87-6f9f-4478-a005-028d1cede6c5.png)
![](https://user-images.githubusercontent.com/105117965/168019210-fa62c667-fc17-4e74-b73f-17be7c2217c6.png)

---
<작성 페이지>
![](https://user-images.githubusercontent.com/105117965/168013150-09632229-d319-494b-9fc5-0a437562217f.png)

---
## 프로젝트 개요 

### 개발기간

- 22.05.09(월) ~ 05.12(목)
- 4일간(기획 1일, 개발 3일)

### 전체일정 프로세스
- 1일차 
: 프로젝트 기획, 기능 선정, 역할분담, 튜터피드백
- 2일차 
: 로그인, 회원가입, 작성페이지, 메인페이지 뼈대 구현 
- 3일차 
: 작성 기능, 사진첨부 기능, 화면 CSS, 모달 기능  
- 4일차 
: Git 병합, AWS 연동, 화면 CSS, 에러 해결, 도메인 연결, 서비스 테스트, 영상 제작 

---
 
### 서비스 기능
** 1. 로그인 페이지**
- 회원가입시 암호화되어 저장된 비밀번호와 로그인 시 받은 비밀번호를 해시함수를 통해 인코딩하여 비교
- DB에 ID와 비밀번호가 일치하는 유저가 있으면 JWT토큰을 받아오는 인증방식으로 구성


** 2. 회원가입 페이지**
- ajax의 POST 방식으로 사용자가 회원가입을 위해 입력한 정보를 DB에 저장
- 비밀번호와 아이디는 조건에 만족하는 경우만 최종적으로 회원가입 가능 및 정규표현식 사용


** 3. 메인페이지**
- 회원들이 리뷰를 작성할 경우 Home페이지에서 노출
- 로그아웃 및 포스팅 버튼 활성화


** 4. 글쓰기 페이지**
- 부트스트랩에서 제공하는 폼을 기반으로 제목, 장소, 사진파일, 상세정보를 담을 수 있는 페이지를 제작
- 플라스크로 API를 관리


### 구현기능

- 로그인 기능
- 회원가입 기능
- 리뷰 작성 기능 
- 사진 첨부 기능
- Feed 모아보기
- 모달 기능


### 사용도구
- HTML, CSS
- JavaScript - Ajax
- Python - pymongo, flask, jwt, datetime, bs4, requests
- AWS EC2


---
  
### 너알맛 API 설계하기
![]()

