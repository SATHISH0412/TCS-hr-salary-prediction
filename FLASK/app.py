import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle
import os
print(os.getcwd())  # Print current working directory
print(os.listdir())  # Print a list of files in the current working directory

app=Flask(__name__)
model=pickle.load(open('hr.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/Prediction',methods=['POST','GET'])
def prediction():
    return render_template('index.html')
@app.route('/Home',methods=['POST','GET'])
def my_home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
 def submit():
    age = request.form['age']
    experience = request.form['experience']
    variables = [[int(age), int(experience)]]
    result = model.predict(variables)
    fin = int(result)

    return render_template('result.html', salary=fin)


if __name__=='__main__':
    app.run(debug=False)
