from flask import Flask

app= Flask(__name__)
@app.route("/")
def home():
    return "Hello user ! this is my first flask app"

@app.route("/about")
def about():
    return "this is about page"

@app.route("/contact")
def contact():
    return "this is contact page "
