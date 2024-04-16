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

if __name__ == '__main__':
   app.run(debug = True)