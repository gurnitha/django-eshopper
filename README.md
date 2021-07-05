# django-eshopper
This is my exercise building ecommerce application based on the tutorial made by Knowledge of Codding on Youtube

https://www.youtube.com/watch?v=M1OdF9U47_c&list=PLTV1jAY3nKHOqKs4uDaBOdqL3jKK7fjSo&index=16

#### 1. Setup - Create venv, install django create project and app

#### 2. Setup static files, templates and homepage

        modified:   README.md
        new file:   apps/home/urls.py
        modified:   apps/home/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        ...
        new file:   static/js/main.js
        new file:   static/js/price-range.js
        new file:   templates/home/index.html

#### 3. Adding html template to home page

        modified:   README.md
        new file:   static/images/ico/favicon.ico
        new file:   static/images/ico/favicon2.ico
        modified:   templates/home/index.html

#### 4. Creating base template and refactoring the home page 

        modified:   README.md
        new file:   templates/base.html
        modified:   templates/home/index.html

#### 5. Create Category and SubCategory models, run migrations and add some data to category

        modified:   apps/home/admin.py
        new file:   apps/home/migrations/0001_initial.py
        modified:   apps/home/models.py

#### 6. Adding data to subcategory        

        modified:   apps/home/models.py
        modified:   README.md

#### 7. Fetching Category and Subcategory data to home page

        modified:   README.md
        modified:   apps/home/views.py
        modified:   templates/home/index.html

#### 8. Create Product model and add products data

        modified:   README.md
        modified:   apps/home/admin.py
        new file:   apps/home/migrations/0002_product.py
        new file:   apps/home/migrations/0003_auto_20210705_0123.py
        modified:   apps/home/models.py

#### 9. Setup media root and add some products

        modified:   README.md
        modified:   apps/home/admin.py
        new file:   apps/home/migrations/0002_product.py
        new file:   apps/home/migrations/0003_auto_20210705_0123.py
        modified:   apps/home/models.py
        modified:   config/urls.py
        new file:   products/img/product1.jpg
        new file:   products/img/product2.jpg
        new file:   products/img/product3.jpg
        new file:   products/img/product4.jpg
        new file:   products/img/product5.jpg
        new file:   products/img/product6.jpg

#### 10. Fetching products to home page from database

        modified:   README.md
        modified:   apps/home/views.py
        modified:   templates/home/index.html

#### 11. Linking categories, subcategories with products

        modified:   README.md
        modified:   apps/home/views.py
        new file:   products/img/adidas-shoes-run.PNG
        new file:   products/img/nike-tshirt.png
        new file:   products/img/nike-tshirt2.png
        new file:   products/img/nike-tshirt3.png
        new file:   products/img/nike-tshirt4.png
        new file:   products/img/uder-armour-activewear.jpg
        new file:   products/img/under-armour-sling-bag.PNG
        new file:   products/img/vandi-patns-b.PNG
        new file:   products/img/vandi-patns-b_HQNI0FA.PNG
        new file:   products/img/vandi-patns-c.PNG
        new file:   products/img/vandi-patns-c_Dd5QEW4.PNG
        new file:   products/img/vandi-patns-d.PNG
        new file:   products/img/vandi-patns-d_ghGF4HS.PNG
        modified:   templates/home/index.html