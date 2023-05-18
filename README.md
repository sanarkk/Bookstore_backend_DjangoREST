# Bookstore Backend
*Project created by using Django Rest Framework technologies*

## About

This backend was developed for book store where users can order and sell books.

## How to start

- pip install -r requirements.txt
- cd backend/
- ./manage.py makemigrations
- ./manage.py migrate
- ./manage.py runserver

## Routes

- 127.0.0.1:8000/main/ ---> *Page which displays all books.*
- 127.0.0.1:8000/create/ ---> *Page which allows to place book for sale, but only after completed auth.*
- 127.0.0.1:8000/update/<book_id>/ ---> *Page which allows to update information about book which you placed, but only after completed auth and authotiry verification.*
- 127.0.0.1:8000/main/<book_id>/ ---> *Page which allows to check information about certain book, but only after completed auth.*
- 127.0.0.1:8000/order/<book_id>/ ---> *Page which allows to order certain book, but only after completed auth.*
- 127.0.0.1:8000/my-profile/ ---> *Page which allows to see information about profile, but only after completed auth.*
- 127.0.0.1:8000/my-orders/ ---> *Page which displays all books which the user ordered.*
- 127.0.0.1:8000/my-orders/[POST] ---> *Page which allows to clear own history of orders.*
- 127.0.0.1:8000/auth/register/ ---> *Page which allows to register an account.*
- 127.0.0.1:8000/auth/login/ ---> *Page which allows to login.*
- 127.0.0.1:8000/auth/logout/ ---> *Page which allows to logout.*
- 127.0.0.1:8000/admin/ ---> *Page which allows to access tables and data by admin panel, but only after admin auth.*

## How to create an admin account

- Make sure that you are in 'backend/' directory
- ./manage.py createsuperuser

## Learn more about technologies

Learn more about [Django Rest Framework](https://www.django-rest-framework.org/)

<sup>created by sanarkk</sup>
