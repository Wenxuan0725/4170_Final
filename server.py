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

@app.route('/quiz/1')
def quiz_1():
    return render_template('quiz_1.html')

@app.route('/quiz/2')
def quiz_2():
    return render_template('quiz_2.html')

@app.route('/quiz/3')
def quiz_3():
    return render_template('quiz_3.html')

@app.route('/quiz/4')
def quiz_4():
    return render_template('quiz_4.html')

@app.route('/quiz/5')
def quiz_5():
    return render_template('quiz_5.html')

@app.route('/quiz/6')
def quiz_6():
    return render_template('quiz_6.html')

@app.route('/quiz/7')
def quiz_7():
    return render_template('quiz_7.html')

@app.route('/quiz/8')
def quiz_8():
    return render_template('quiz_8.html')

@app.route('/quiz/end')
def quiz_end():
    return render_template('quiz_end.html')

if __name__ == '__main__':
   app.run(debug = True)