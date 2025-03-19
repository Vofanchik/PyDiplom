# Backend-приложение для автоматизации закупок на Django Rest Framework

## Запуск сервера
```bash
python manage.py makemigrations store user # инициализация миграций из моделей приложений
python manage.py migrate # применение миграций к БД
python manage.py createsuperuser # создание учётной записи администратора (e.g. login:admin@admin.ru; password: admin)
python manage.py runserver # запуск сервера
```
## Работа с API
Далее на примере сервиса для работы с API **Postman**  
> базовый url \<baseurl\> = http://127.0.0.1:8000, для изменения `manage.py runserver 0.0.0.0:<your_port>`  
### Получение токена:  
**POST:** \<baseurl\>/api-token-auth/  
**Notes:**  
```json
{
    "username": "Логин",
    "password": "Пароль" 
}
```
**Body:**  
```json
{
    "username": "admin@admin.ru",
    "password": "admin" 
}
```
**Response:**  
```json
{
    "token": "8d94004f09ac227fb498a3f7ad4657aca0fce9db"
}
```
> ***!!! Для авторизации, необходимо передать токен в заголовоки запроса (headers) в формате:***
> ```json
> headers: {
>    "Authorization": "Token 165e7922ca701b983f749eec1c2ee146b378cad9"
> }
>  ```

### Регистрация участника:  
**POST:** \<baseurl\>/register/  
**Notes:**  
```json
{
    "email": "эл. почта", 
    "type": "тип участника ('shop' - 'Магазин, 'buyer' - 'Покупатель')", 
    "first_name": "Имя", 
    "last_name": "Фамилия", 
    "patronymic": "Отчество", 
    "company": "Название компании", 
    "position": "Должность", 
    "password": "пароль", 
    "password2": "повторить пароль для подтверждения"
}
```
**Body:**  
```json
{
    "email": "test@test.ru", 
    "type": "shop", 
    "first_name": "Иван", 
    "last_name": "Иванов", 
    "patronymic": "Иванович", 
    "company": "Test_company", 
    "position": "", 
    "password": "test", 
    "password2": "test"
}
```
**Response:**  
```json
{
    "response": true
}
```

### Добавление товаров через yaml:  
**POST:** \<baseurl\>/partner/update
**Notes:**  
```json
{
    "file":"путь к файлу",
    "url": "url файла"
}
```
**Body:**  
```json
{
    "file":"shop.yaml"
}
```
**Response:**  
```json
{
    "response": true
}
```

## Схема БД
![](Assets/db_lite.sqlite3.png)