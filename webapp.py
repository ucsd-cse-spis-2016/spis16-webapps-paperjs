import os
from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def render_main():
    return render_template('home.html')

@app.route('/page1')
def render_page1():
    return render_template('page1.html')

@app.route('/page2')
def render_page2():
    return render_template('page2.html')


# You'll probably want a basic function here to convert miles to kilometers too...

if __name__=="__main__":
    app.run(debug=False, port=54321)
