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

  

## 3. 프로젝트 구조 및 플로우 차트

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



### 3.2 플로우 차트
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
