import os
import pandas as pd
from flask import Flask, render_template, send_from_directory, request, redirect
app = Flask(__name__)

#Funcion que agrega informacion a un txt
def csv(email,subject,message):
    file = pd.read_csv(r'C:\Users\lenovo\Documents\Daniel\Cursos\Udemy\Python\Section 19 - Web Development with Python\venv\database.csv',sep='|')
    data = {'email':email,'subject':subject,'message':message}
    file = file.append(data,ignore_index=True)
    file.to_csv(r'C:\Users\lenovo\Documents\Daniel\Cursos\Udemy\Python\Section 19 - Web Development with Python\venv\database.csv',sep='|',index=None)

#End points e.g.
@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET']) #El end point apunta a contact linea 62.
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        csv(data['email'],data['subject'],data['message'])
        return redirect('thankyou.html')
    else:
        return 'oops'