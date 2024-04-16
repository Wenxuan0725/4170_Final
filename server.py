from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('Homepage.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/learn/1')
def learn_step1():
    return render_template('learn_step1.html')

@app.route('/learn/2')
def learn_step2():
    return render_template('learn_step2.html')

@app.route('/learn/2.1')
def learn_step2_1():
    return render_template('learn_step2_1.html')

@app.route('/learn/3')
def learn_step3():
    return render_template('learn_step3.html')

if __name__ == '__main__':
   app.run(debug = True)