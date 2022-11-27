import requests
from flask import Flask, render_template, request
import psycopg2


app = Flask(__name__)
conn = psycopg2.connect(database="Service_db", user="postgres", password="1", host="localhost", port="5432")
cursor = conn.cursor()

@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/login/', methods=['POST','GET'])
def login():
    if request.method =="POST": #берем значения у пользователя
        username = request.form.get('username')
        password = request.form.get('password')
    if username=='' or password=='': #проверяем значения на пустые поля
        return render_template('error.html')
    try:
        cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password))) #сравниваем пользовательские данные и данные из базы
        records = list(cursor.fetchall()) #сведения из базы данных преобразуются в кортежи
        return render_template('Accounts.html', full_name=records[0][1], username=username, password=password)
    except:
        return render_template('error2.html')

