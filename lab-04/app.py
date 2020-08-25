from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


# your code here
@app.route('/')
def home():
    return render_template('home.template.html')


@app.route('/greet')
def greet():
    first_name = "John"
    last_name = "Smith"
    return render_template('greeting.template.html',
                           fname=first_name, lname=last_name)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
