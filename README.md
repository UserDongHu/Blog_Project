# Django Blog Project - Hot🔥Deal Blog
  * 다양한 핫딜 정보를 게시할 수 있는 블로그 입니다.
  * 카테고리별로 다양한 핫딜 정보를 볼 수 있습니다.
    
## 1. 목표와 기능
  1.1 목표

  * Django를 통해 핫딜 정보를 게시할 수 있는 블로그 개발
  * Accounts와 CRUD 기능을 CBV로 구현
  * BootStrap을 이용하여 깔끔하게 UI 꾸미기
  * 알고있는 핫딜 정보를 공유할 수 있습니다.
  * 평소에 갖고싶던 물건을 이 블로그의 정보를 통해서 더 합리적으로 구매할 수 있습니다.

1.2 기능

  * 회원가입 후, 로그인을 해서 게시글을 올릴 수 있습니다.
  * 게시글에서 상세 정보를 볼 수 있고 추천과 비추천, 댓글을 통해 의견을 나눌 수 있습니다.
  * 내가 쓴 글과 댓글을 단 글, 추천을 한 글을 볼 수 있습니다.
## 2. Stacks
  
  * Enviroment

    ![VSC](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
    ![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
    ![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

 

  * Development


    ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
    ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
    ![BootStrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
 


  * DataBase
    
    ![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

  

## 3. 프로젝트/URL 구조 및 플로우 차트

  ### 3.1 프로젝트 구조
  
* accounts와 blog 두개의 앱으로 구성
* media, static, templates폴더를 root에 배치
```  
myblog
├── accounts
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── blog
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── media
│   └── blog
│       ├── files
│       └── thumb_images
├── projectdjango
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static
│   ├── assets
│   │   └── favicon.ico
│   ├── css
│   │   └── styles.css
│   ├── index.html
│   └── js
│       └── scripts.js
└── templates
    ├── accounts
    │   ├── form.html
    │   └── profile.html
    └── blog
        ├── addreplyform.html
        ├── editcommentform.html
        ├── menu.html
        ├── post_confirm_delete.html
        ├── post_detail.html
        ├── post_list.html
        └── postform.html
```

### 3.2 URL 구조
#### accounts
* '/accounts/signp' : 회원가입
* '/accounts/login' : 로그인
* '/accounts/logout' : 로그아웃
* '/accounts/profile' : 내 프로필

#### blog
* '/blog' : 모든 게시글 보기
* '/blog/mypost' : 내가 쓴 게시글 보기
* '/blog/mycomment' : 내가 댓글 쓴 게시물 보기
* '/blog/myhits' : 내가 추천 누른 게시물 보기
* '/blog/create' : 게시글 생성
* '/blog/<int:pk>' : 게시물 상세 보기
* '/blog/<int:pk>/edit' : 게시물 수정
* '/blog/<int:pk>/delete' : 게시물 삭제
* '/blog/comment/create/<int:pk>' : 댓글 생성
* '/blog/comment/edit/<int:pk>' : 댓글 수정
* '/blog/reply/create/<int:pk>' : 대댓글 생성
* '/blog/hits/post/<int:pk>' : 게시글 추천
* '/blog/unhits/post/<int:pk>' : 게시글 비추천
* '/blog/hits/comment/<int:pk>' : 댓글 추천
* '/blog/unhits/comment/<int:pk>' : 댓글 비추천

### 3.3 플로우 차트
* 메인페이지에서 크게 로그인/회원가입과 게시물보기를 선택할 수 있습니다.
* 로그인이 된 유저만 게시물쓰기, 추천, 댓글달기 등을 할 수 있습니다.
<img width="1127" alt="image" src="https://github.com/UserDongHu/Blog_Project/assets/137512514/033478cb-297b-4555-89ad-0c159302285b">





## 4. WBS
* 2023.10.26 ~ 2023.11.7
<img width="1109" alt="image" src="https://github.com/UserDongHu/Blog_Project/assets/137512514/46094cf6-d052-407e-a632-d481453e0452">




## 5. ERD 
* User, Post, Comment, Category로 4개의 테이블로 구성
* User과 Post, User과 Comment, Post와 Comment를 1:N 관계로 연결
* Post와 Category는 N:N 관계로 연결
* Comment에 parent_comments_id를 이용해서 대댓글을 구현
<img width="783" alt="image" src="https://github.com/UserDongHu/Blog_Project/assets/137512514/b081be7e-4b19-49f2-aadf-275f10afbef3">







## 6. UI 
* 메인화면에서 회원가입과 로그인
![Signup_Login](https://github.com/UserDongHu/Blog_Project/assets/137512514/7d4cc815-1345-4f1a-a513-2c802be0d247)
<br></br>
* 카테고리별로 보기
![Post_list](https://github.com/UserDongHu/Blog_Project/assets/137512514/bfd4296d-b710-4396-be2f-acbbb248f20c)
<br></br>
* 게시물 작성하기
* 로그인된 유저만 작성할 수 있음
![CreatePost](https://github.com/UserDongHu/Blog_Project/assets/137512514/a2379174-a738-422a-98f9-263a978025e2)
<br></br>
* 게시물 추천, 비추천 기능과 게시물 수정
* 로그인된 유저만 추천, 비추천 할 수 있고 본인이 쓴 게시물만 수정 가능
![EditPost](https://github.com/UserDongHu/Blog_Project/assets/137512514/077e82b9-3e0c-4191-8f53-8e86414ea534)
<br></br>
* 게시물 상세보기, 댓글 작성
* 게시물의 상품명 또는 이미지를 클릭하면 상품 링크로 연결
* 로그인된 유저만 댓글을 작성할 수 있음
![PostDetail+CreateComment](https://github.com/UserDongHu/Blog_Project/assets/137512514/1a21eb57-fb6b-4702-8bba-bb8c56009360)
<br></br>
* 댓글 추천, 비추천 기능과 대댓글 작성
* 로그인된 유저만 댓글을 추천, 비추천 할 수 있고 대댓글을 작성할 수 있음
![HitComment+CreateReply](https://github.com/UserDongHu/Blog_Project/assets/137512514/a208af64-cc95-43dd-ab63-9a09982374af)
<br></br>
* 댓글, 대댓글 수정
* 내가 쓴 댓글 또는 대댓글만 수정 가능
![Edit comment](https://github.com/UserDongHu/Blog_Project/assets/137512514/199c57e8-77ad-4eca-9007-22bbe7ff64e1)
<br></br>
* 프로필에서 내가 쓴 게시물, 내가 댓글 쓴 게시물, 내가 추천한 게시물 보기
![Profile+mypost+commentpost+hitpost](https://github.com/UserDongHu/Blog_Project/assets/137512514/9f2436f2-50a0-4c5a-99e9-600f36ec9689)
<br></br>
* 게시물 리스트에서 검색하기
* 제목, 내용, 댓글, 작성자 등으로 검색할 수 있음
![Search](https://github.com/UserDongHu/Blog_Project/assets/137512514/afd191b3-f07d-4bb7-a3ac-301a8a25140d)
