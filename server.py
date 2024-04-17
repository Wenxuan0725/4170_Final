from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

current_score = 0

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
    global current_score
    current_score = 0
    return render_template('quiz_start.html')

@app.route('/quiz/1')
def quiz_1():
    global current_score
    return render_template('quiz_1.html', current_score=current_score)


@app.route('/quiz/2')
def quiz_2():
    global current_score
    return render_template('quiz_2.html', current_score=current_score)

@app.route('/quiz/3')
def quiz_3():
    global current_score
    return render_template('quiz_3.html', current_score=current_score)

@app.route('/quiz/4')
def quiz_4():
    global current_score
    return render_template('quiz_4.html', current_score=current_score)

@app.route('/quiz/5')
def quiz_5():
    global current_score
    return render_template('quiz_5.html', current_score=current_score)

@app.route('/quiz/6')
def quiz_6():
    global current_score
    return render_template('quiz_6.html', current_score=current_score)

@app.route('/quiz/7')
def quiz_7():
    global current_score
    return render_template('quiz_7.html', current_score=current_score)

@app.route('/quiz/8')
def quiz_8():
    global current_score
    return render_template('quiz_8.html', current_score=current_score)

@app.route('/quiz/end')
def quiz_end():
    global current_score
    score = current_score

    if score >= 90:
        message = "Congratulations! You've mastered all the quizzes, showcasing your exceptional skills and understanding. Your hard work and perseverance have truly paid off. We're so proud of what you've accomplished! It’s time for you to set up a tent on your next trip."
    elif score >= 70:
        message = "Great job! You have a solid understanding of the material, but there's still some room for improvement. Keep studying, and you're sure to master everything!"
    elif score >= 50:
        message = "Good effort! You've grasped the basics, but you need to work on some areas to fully master the material. Consider reviewing the topics again."
    else:
        message = "It looks like you need some more practice. Don't worry, review the material and try the quiz again. You can improve!"

    return render_template('quiz_end.html', score=score, message=message)




@app.route('/submit_answer/<int:question_id>', methods=['POST'])
def submit_answer(question_id):
    global current_score
    data = request.get_json()
    answer_score = data['answer_score']
    
    
    current_score += answer_score

    return jsonify({'score': current_score})

@app.route('/reset_score', methods=['GET'])
def reset_score():
    global current_score
    current_score = 0
    return jsonify({'message': 'Score reset successfully'})


if __name__ == '__main__':
   app.run(debug = True)