# Web-technologies
Stepik.org mail.ru course

# QA application (MVC structure)
Само приложение находится внутри папки ASK.  
  
Router: ask/ask/urls.py (маршрутизация URL)  
View: ask/qa/templates/question/ (генерация примитивного представления в виде HTML)  
Model: ask/qa/models.py (работа с объектами и БД (ORM))  
Controller: ask/qa/views.py (работа с http и связь с объектами БД и представления)  
  
Если не сталкивались с Django, то пусть не смущает наименование файлов.    
Вопреки наименованиям в паттерне MVC, в Django они именуются по-своему.  
Например: 
Controller хранится в файле views.py, но он не выполняет функцию представления View.  
View выполняется из папки templates по соглашению Django.  
  
### Это важно:
Для запуска приложения использовался Nginx сервер, который проксирует запросы на бэкэнд приложение развёрнутое на Gunicorn.  
Всё это было развёрнуто на Ubuntu, на котором было установлено MySQL.  
  
To run this app use:
### ask/initask.sh

