# Bookstore Backend
*Project created by using Django Rest Framework technologies*

## About

This backend was developed for book store where users can order and sell books.

## How to run the project
```
git clone https://github.com/sanarkk/Bookstore-backend-DRF.git
```
```
cd Bookstore-backend-DRF/
```
```
docker-compose up
```

## Routes

- This project has configured Swagger, thus in order to see routes just run the project and open 127.0.0.1:8000.

## How to access to tables and data by using Admin page

```
docker exec -it backend-bookstore-drf-backend-1 bash
```
```
./manage.py createsuperuser
```
```
exit
```

## Learn more about technologies

Learn more about [Django Rest Framework](https://www.django-rest-framework.org/)

<sup>created by sanarkk</sup>
