from flask import Flask, render_template, request,redirect, url_for, flash

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template('login.html')
   
@app.route("/registration")
def registration():
    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True)