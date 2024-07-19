# stparthr
Technical specifications for Junior Python developer from Guider.pro. Service that processes and responds to HTTP requests - stparthr

### Инструкции по установке и использованию будут написаны на русском языке, чтобы избежать ошибок и недопониманий.

## Автор проекта:
### Денисов Александр Евгеньевич
### GitHub [SkullPiercer](https://github.com/)

## Стек:
```python
  Django==3.2.16
```
```python
  djangorestframework==3.12.4
```
```python
  djangorestframework-simplejwt==4.7.2
```
```python
  djoser==2.1.0
```
# Как запустить проект.
### **Клонировать репозиторий и перейти в него в командной строке:**
```python 
  git clone git@github.com:SkullPiercer/stparthr.git
```
```python
  cd stparthr
```
### **Cоздать и активировать виртуальное окружение:**
#### Windows:
```python
  python -m venv venv
```
```python
  source venv/Scripts/activate
```
#### Linux/Mac:
```python
  python3 -m venv env
```
```python
  source env/bin/activate
```
### **Установить зависимости из файла requirements.txt:**
#### Windows:
```python
  python -m pip install --upgrade pip
```
```python
  pip install -r requirements.txt
```
#### Linux/Mac
```python
  python3 -m pip install --upgrade pip
```
```python
  pip install -r requirements.txt
```
### **Установить секретный ключ:**
#### В директории с файлом settings.py необходимо создать файл .env и поместить в него 
```python
SECRET_KEY=django-insecure-+c2u4te3548!43hznu*((_5na7jshq))ts2joyo$5ta@4f3(tn
```
### **Выполнить миграции:**
#### Windows:
```python
  python manage.py migrate
```
#### Linux/Mac
```python
  python3 manage.py migrate
```
### **Установить фикстуры:**
#### Windows:
```python
  python manage.py loaddata fixtures.json

```
#### Linux/Mac
```python
  python3 manage.py loaddata fixtures.json
```
### **Запустить проект:**
#### Windows:
```python
  python manage.py runserver
```
#### Linux/Mac:
```python
  python3 manage.py runserver
```
### **Информация по эндпоинтам есть в:**
```python
  http://127.0.0.1:8000/redoc/
```
```python
  http://127.0.0.1:8000/swagger/
```
## Порядок действий для регистрации и получения токена:
### для начала регестрируемся в системе туда передаем username и password http://127.0.0.1:8000/auth/users/

### Потом на эндпоинте http://127.0.0.1:8000/auth/jwt/create/ Получаем JWT токен и вставляем его в заголовки запросов

