import pickle

from flask import Flask, render_template, request

app = Flask(__name__)
model = pickle.load(open('hr.pkl', 'rb'))


@app.route('/')
def entry():
    return render_template('home.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/index')
def predict():
    return render_template('index.html')


@app.route('/getdata', methods=['POST'])
def submit():
    age = request.form['age']
    experience = request.form['experience']
    variables = [[int(age), int(experience)]]
    result = model.predict(variables)
    fin = int(result)

    return render_template('result.html', salary=fin)


if __name__ == "__main__":
    app.run(debug=True)
