## BUILDING ECOMMERCE Hmart USING DJANGO V3.2


### 1. SETUP STATIC 

#### 1.1 Complete (project, app, db) setup with home page

        ..for-kuningan$ tree -L 3
        .
        └── src
            ├── README.md
            ├── apps
            │   ├── home
            ├── config
            │   ├── __init__.py
            │   ├── __pycache__
            │   ├── asgi.py
            │   ├── settings.py
            │   ├── static
            │   ├── urls.py
            │   └── wsgi.py
            ├── manage.py
            └── templates
                ├── base.html
                └── shared
        
        new file:   .gitignore
        new file:   README.md


#### 1.2 Create shop app and products list

        ..for-kuningan$ tree -L 3
        .
        └── src
            ├── README.md
            ├── apps
            │   ├── home
            │   ├── shop # <-- here
            ├── config
            │   ├── __init__.py
            │   ├── __pycache__
            │   ├── asgi.py
            │   ├── settings.py
            │   ├── static
            │   ├── urls.py
            │   └── wsgi.py
            ├── manage.py
            └── templates
                ├── base.html
                └── shared
        
        new file:   .gitignore
        new file:   README.md


#### 1.3 Showing single product

        modified:   README.md
        new file:   apps/shop/templates/inc/breadcrumb-single.html
        modified:   apps/shop/templates/inc/products.html
        new file:   apps/shop/templates/shop/product.html
        modified:   apps/shop/urls.py
        modified:   apps/shop/views.py


#### 1.4 Create blog app and posts list

        ..for-kuningan$ tree -L 3
        .
        └── src
            ├── README.md
            ├── apps
            │   ├── home
            │   ├── shop
            │   ├── blog # <-- here
            ├── config
            │   ├── __init__.py
            │   ├── __pycache__
            │   ├── asgi.py
            │   ├── settings.py
            │   ├── static
            │   ├── urls.py
            │   └── wsgi.py
            ├── manage.py
            └── templates
                ├── base.html
                └── shared
        
        modified:   README.md
        ...
        modified:   apps/shop/templates/inc/breadcrumb-single.html
        modified:   apps/shop/templates/inc/breadcrumb.html
        modified:   config/settings.py
        modified:   config/urls.py
        modified:   templates/shared/header.html


#### 1.5 Showing single post

        modified:   README.md
        new file:   apps/blog/templates/blog/post.html
        new file:   apps/blog/templates/inc/breadcrumb-blog-single.html
        new file:   apps/blog/templates/inc/comment-blog.html
        new file:   apps/blog/templates/inc/post.html
        modified:   apps/blog/templates/inc/posts.html
        modified:   apps/blog/urls.py
        modified:   apps/blog/views.py


#### 1.6 Create about app and about page

        ..for-kuningan$ tree -L 3
        .
        └── src
            ├── README.md
            ├── apps
            │   ├── about # <-- here
            │   ├── home
            │   ├── blog
            │   ├── shop
            ├── config
            │   ├── __init__.py
            │   ├── __pycache__
            │   ├── asgi.py
            │   ├── settings.py
            │   ├── static
            │   ├── urls.py
            │   └── wsgi.py
            ├── manage.py
            └── templates
                ├── base.html
                └── shared

        modified:   README.md
        ..
        modified:   config/settings.py
        modified:   config/urls.py
        modified:   templates/shared/header.html


#### 1.7 Create contact app and contact page

        ..for-kuningan$ tree -L 3
        .
        └── src
            ├── README.md
            ├── apps
            │   ├── about
            │   ├── blog
            │   ├── contact # <-- here
            │   ├── home
            │   ├── shop
            ├── config
            │   ├── __init__.py
            │   ├── __pycache__
            │   ├── asgi.py
            │   ├── settings.py
            │   ├── static
            │   ├── urls.py
            │   └── wsgi.py
            ├── manage.py
            └── templates
                ├── base.html
                └── shared
        modified:   README.md
        ...
        modified:   config/settings.py
        modified:   config/urls.py
        modified:   templates/shared/header.html


#### 1.8 Create account app and login-register page


        ..for-kuningan$ tree -L 3
        .
        └── src
            ├── README.md
            ├── apps
            │   ├── about
            │   ├── account # <-- here
            │   ├── blog
            │   ├── contact
            │   ├── home
            │   ├── shop
            ├── config
            │   ├── __init__.py
            │   ├── __pycache__
            │   ├── asgi.py
            │   ├── settings.py
            │   ├── static
            │   ├── urls.py
            │   └── wsgi.py
            ├── manage.py
            └── templates
                ├── base.html
                └── shared

        modified:   README.md
        ...
        modified:   config/settings.py
        modified:   config/urls.py
        modified:   templates/shared/header.html


#### 1.9 Create profile page

        modified:   README.md
        new file:   apps/account/templates/account/profile.html
        new file:   apps/account/templates/inc/breadcrumb-profile.html
        new file:   apps/account/templates/inc/profile.html
        modified:   apps/account/urls.py
        modified:   apps/account/views.py
        modified:   templates/shared/header.html


#### 1.10 Complete project structures

        for-kuningan/src$ tree -L 3
        .
        ├── README.md
        ├── apps
        │   ├── about
        │   │   ├── __init__.py
        │   │   ├── __pycache__
        │   │   ├── admin.py
        │   │   ├── apps.py
        │   │   ├── migrations
        │   │   ├── models.py
        │   │   ├── templates
        │   │   ├── tests.py
        │   │   ├── urls.py
        │   │   └── views.py
        │   ├── account
        │   │   ├── __init__.py
        │   │   ├── __pycache__
        │   │   ├── admin.py
        │   │   ├── apps.py
        │   │   ├── migrations
        │   │   ├── models.py
        │   │   ├── templates
        │   │   ├── tests.py
        │   │   ├── urls.py
        │   │   └── views.py
        │   ├── blog
        │   │   ├── __init__.py
        │   │   ├── __pycache__
        │   │   ├── admin.py
        │   │   ├── apps.py
        │   │   ├── migrations
        │   │   ├── models.py
        │   │   ├── templates
        │   │   ├── tests.py
        │   │   ├── urls.py
        │   │   └── views.py
        │   ├── contact
        │   │   ├── __init__.py
        │   │   ├── __pycache__
        │   │   ├── admin.py
        │   │   ├── apps.py
        │   │   ├── migrations
        │   │   ├── models.py
        │   │   ├── templates
        │   │   ├── tests.py
        │   │   ├── urls.py
        │   │   └── views.py
        │   ├── home
        │   │   ├── __init__.py
        │   │   ├── __pycache__
        │   │   ├── admin.py
        │   │   ├── apps.py
        │   │   ├── migrations
        │   │   ├── models.py
        │   │   ├── templates
        │   │   ├── tests.py
        │   │   ├── urls.py
        │   │   └── views.py
        │   └── shop
        │       ├── __init__.py
        │       ├── __pycache__
        │       ├── admin.py
        │       ├── apps.py
        │       ├── migrations
        │       ├── models.py
        │       ├── templates
        │       ├── tests.py
        │       ├── urls.py
        │       └── views.py
        ├── config
        │   ├── __init__.py
        │   ├── __pycache__
        │   │   ├── __init__.cpython-39.pyc
        │   │   ├── settings.cpython-39.pyc
        │   │   ├── urls.cpython-39.pyc
        │   │   └── wsgi.cpython-39.pyc
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── static
        │   │   └── assets
        │   ├── urls.py
        │   └── wsgi.py
        ├── contact-form.html
        ├── contact-map.html
        ├── manage.py
        └── templates
            ├── base.html
            └── shared
                ├── footer.html
                ├── head.html
                ├── header.html
                ├── modal-addtocart.html
                ├── modal-compare.html
                ├── modal-quickview.html
                ├── modal-wishlist.html
                ├── off-canvas.html
                └── scripts.html