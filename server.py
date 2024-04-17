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

@app.route('/learn/2.2')
def learn_step2_2():
    return render_template('learn_step2_2.html')

@app.route('/learn/2.3')
def learn_step2_3():
    return render_template('learn_step2_3.html')

@app.route('/learn/2.4')
def learn_step2_4():
    return render_template('learn_step2_4.html')

@app.route('/learn/2.5')
def learn_step2_5():
    return render_template('learn_step2_5.html')

@app.route('/learn/2.6')
def learn_step2_6():
    return render_template('learn_step2_6.html')

@app.route('/learn/3')
def learn_step3():
    return render_template('learn_step3.html')

@app.route('/learn/3.1')
def learn_step3_1():
    return render_template('learn_step3_1.html')

@app.route('/learn/3.2')
def learn_step3_2():
    return render_template('learn_step3_2.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz_start.html')

@app.route('/q2')
def q2():
    return render_template('q2.html')

@app.route('/q3')
def q3():
    return render_template('q3.html')

@app.route('/q4')
def q4():
    return render_template('q4.html')

@app.route('/q5')
def q5():
    return render_template('q5.html')

@app.route('/q6')
def q6():
    return render_template('q6.html')

@app.route('/q7')
def q7():
    return render_template('q7.html')

@app.route('/q8')
def q8():
    return render_template('q8.html')

if __name__ == '__main__':
   app.run(debug = True)