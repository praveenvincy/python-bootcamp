from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #fruits=['apple','banana','grape','apricot']

    return render_template('index.html')#,quote='the key to life is happiness in your household',fruits=fruits)

# @app.route('/about')
# def about():
#     return '<h1>Hello World from about page </h1>'

@app.route('/quote')
def quote():
    return render_template('quote.html')

