# 2022-django-blog-flattern
This is my exercise based on the template I downloaded from https://www.free-css.com/



### PART 1: SETTING UP FULLY STATIC PAGES IN DJANGO
---------------------------------------------------


#### 1. Create django project, blog app and portfolio app

        STEPS:

        1. Install and check python
        2. Install pip and check pip
        3. Create virtual env
        4. Activate env
        	λ venv39303\scripts\activate
        5. Install django
        	(portfolio) λ pip install django==3.0.3
        6. Create project
        	(portfolio) λ django-admin startproject config . 
        7. Create appsand apps
         	(portfolio) λ mkdir apps
         	(portfolio) λ mkdir apps\portfolio
         	(portfolio) λ mkdir apps\blog
         	(portfolio) λ django-admin startapp blog apps\blog
         	(portfolio) λ django-admin startapp portfolio apps\portfolio
        7. Modify apps.py files 
        8. Register apps to settings.py
        9. Run the server to test it out:
        10. File structures

        E:.
        │   .gitignore
        │   LICENSE
        │   manage.py
        │   README.md
        │
        ├───apps
        │   ├───blog
        │   │   │   admin.py
        │   │   │   apps.py
        │   │   │   models.py
        │   │   │   tests.py
        │   │   │   views.py
        │   │   │   __init__.py
        │   │   │
        │   │   └───migrations
        │   │           __init__.py
        │   │
        │   └───portfolio
        │       │   admin.py
        │       │   apps.py
        │       │   models.py
        │       │   tests.py
        │       │   views.py
        │       │   __init__.py
        │       │
        │       └───migrations
        │               __init__.py
        │
        └───config
                asgi.py
                settings.py
                urls.py
                wsgi.py
                __init__.py


#### 2. Setting Views, Templates, and Urls for home page

        modified:   README.md
        new file:   apps/portfolio/templates/portfolio/index.html
        new file:   apps/portfolio/urls.py
        modified:   apps/portfolio/views.py
        modified:   config/settings.py
        new file:   config/static/contactform/Readme.txt
        ...
        new file:   config/static/skins/yellow.css
        modified:   config/urls.py


#### 3. Extending base template

        modified:   README.md
        modified:   apps/portfolio/templates/portfolio/index.html
        new file:   templates/base.html


#### 4. Removing some menu items

        modified:   README.md
        modified:   templates/base.html


#### 5. Setting Views, Templates, and Urls for portfolio page

        modified:   README.md
        new file:   apps/portfolio/templates/portfolio/portfolio.html
        modified:   apps/portfolio/urls.py
        modified:   apps/portfolio/views.py
        modified:   templates/base.html


#### 6. Setting Views, Templates, and Urls for posts page

        modified:   README.md
        new file:   apps/blog/templates/blog/posts.html
        new file:   apps/blog/urls.py
        modified:   apps/blog/views.py
        modified:   config/urls.py
        modified:   templates/base.html


#### 7. Setting Views, Templates, and Urls for single post page

        modified:   README.md
        modified:   apps/blog/templates/blog/posts.html
        new file:   apps/blog/templates/blog/single.html
        modified:   apps/blog/urls.py
        modified:   apps/blog/views.py


#### 8. House keeping: Modified README.md file

        modified:   README.md



### PART 2: WORKING ON FOR FULLY DYNAMIC PAGES IN DJANGO
--------------------------------------------------------


### 1. SLIDERS
--------------

#### 1.1 Main sliders: Create Slider model, Load data on View and Display data on the slider


        modified:   README.md
        modified:   apps/portfolio/admin.py
        new file:   apps/portfolio/migrations/0001_initial.py
        new file:   apps/portfolio/migrations/0002_auto_20220124_2118.py
        new file:   apps/portfolio/migrations/0003_auto_20220124_2124.py
        modified:   apps/portfolio/models.py
        modified:   apps/portfolio/templates/portfolio/index.html
        modified:   apps/portfolio/views.py
        ...
        new file:   media/sliders/2022/01/24/bg-3.jpg


### 2. COMPANY'S SERVICES
-------------------------

#### 2.1 Company's services: Create Service model, Load data on View and display data on the pada

        modified:   README.md
        modified:   apps/portfolio/admin.py
        new file:   apps/portfolio/migrations/0004_service.py
        modified:   apps/portfolio/models.py
        modified:   apps/portfolio/templates/portfolio/index.html
        modified:   apps/portfolio/views.py


### 3. IMAGES GALLERY
---------------------

#### 3.1 Images Gallery: Create Gallery model, Load data on View and display them to the page

       modified:   README.md
        modified:   apps/portfolio/admin.py
        new file:   apps/portfolio/migrations/0005_gallery.py
        modified:   apps/portfolio/models.py
        modified:   apps/portfolio/templates/portfolio/index.html
        modified:   apps/portfolio/views.py
        new file:   media/gallery/2022/01/25/image-01-full.jpg
        ...
        new file:   media/gallery/2022/01/25/image-08.jpg


### 4. CLIENTS
--------------

#### 4.1 Clients: Create Client model, Load data on View and display them on the page

        modified:   README.md
        modified:   apps/portfolio/admin.py
        new file:   apps/portfolio/migrations/0006_client.py
        modified:   apps/portfolio/models.py
        modified:   apps/portfolio/templates/portfolio/index.html
        modified:   apps/portfolio/views.py
        new file:   media/client/2022/01/25/client1.png
        ...
        new file:   media/client/2022/01/25/client6_7jYDxtb.png


### 5. GALLERY PORTFOLIO
------------------------

#### 5.1 Gallery portfolio: Create Category model, modified Gallery model, load and display on portfolio page

        modified:   README.md
        modified:   apps/portfolio/admin.py
        new file:   apps/portfolio/migrations/0007_auto_20220125_0828.py
        new file:   apps/portfolio/migrations/0008_auto_20220125_0852.py
        new file:   apps/portfolio/migrations/0009_auto_20220125_0856.py
        new file:   apps/portfolio/migrations/0010_auto_20220125_1005.py
        new file:   apps/portfolio/migrations/0011_gallery_is_galery_data_type_webdev.py
        modified:   apps/portfolio/models.py
        modified:   apps/portfolio/templates/portfolio/portfolio.html
        modified:   apps/portfolio/views.py
        new file:   media/gallery/2022/01/25/image-01-full_FpguyQp.jpg
        new file:   media/gallery/2022/01/25/image-01_gL1gxVN.jpg


#### 5.2 Gallery portfolio: Modified point 5.1 for DRY principle

        modified:   README.md
        new file:   apps/portfolio/migrations/0012_auto_20220125_1042.py
        modified:   apps/portfolio/models.py
        modified:   apps/portfolio/templates/portfolio/portfolio.html
        modified:   apps/portfolio/views.py




























































































































































































