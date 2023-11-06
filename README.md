# 핫딜 정보 블로그
  * 다양한 핫딜 정보를 게시할 수 있는 블로그 입니다.
  * 카테고리별로 다양한 핫딜 정보를 볼 수 있습니다.
## 1. 목표와 기능
  1.1 목표

  * 자유롭게 핫딜 정보를 게시할 수 있는 블로그
  * 알고있는 핫딜 정보를 공유할 수 있습니다.
  * 평소에 갖고싶던 물건을 이 블로그의 정보를 통해서 더 합리적으로 구매할 수 있습니다.

1.2 기능

  * 회원가입 후, 로그인을 해서 게시글을 올릴 수 있습니다.
  * 게시글에서 상세 정보를 볼 수 있고 추천과 비추천, 댓글을 통해 의견을 나눌 수 있습니다.
  * 내가 쓴 글과 댓글들을 확인할 수 있습니다.
## 2. 개발 환경
  * Web Framework
    * Django 4.2.6

  * DataBase
    * SQLite3
  

## 3. 프로젝트 구조 및 플로우 차트
  3.1 프로젝트 구조

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
    
  3.2 플로우 차트
  
<img width="1127" alt="image" src="https://github.com/UserDongHu/Blog_Project/assets/137512514/033478cb-297b-4555-89ad-0c159302285b">



## 4. WBS
<img width="1103" alt="image" src="https://github.com/UserDongHu/Blog_Project/assets/137512514/3c49c7f1-acd5-4ce0-9391-2b3c7700c005">



## 5. ERD 
<img width="783" alt="image" src="https://github.com/UserDongHu/Blog_Project/assets/137512514/b081be7e-4b19-49f2-aadf-275f10afbef3">







## 6. UI 
