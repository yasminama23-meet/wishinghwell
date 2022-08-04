rom flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase



Config = {
  "apiKey": "AIzaSyAyHiPFSFyI8M_8SfJaYSoBETfUhlldvFg",
  "authDomain": "wishingwell-7d53a.firebaseapp.com",
  "databaseURL": "https://wishingwell-7d53a-default-rtdb.firebaseio.com",
  "projectId": "wishingwell-7d53a",
  "storageBucket": "wishingwell-7d53a.appspot.com",
  "messagingSenderId": "308934572829",
  "appId": "1:308934572829:web:7ab3dc2485b45a07213ff4",
  "measurementId": "G-QXCYKZ7R2S"
  "databaseURL":""
}



firebase=pyrebase.initialize_app(Config)
auth=firebase.auth()
db=firebase.database()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'



#Code goes below here

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/login')
def loin():
    return render_template('login.html')


@app.route('/about')
def about():
    return render_template('about.html')


#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)