from flask import Flask, render_template, request, redirect, url_for, flash
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
  "measurementId": "G-QXCYKZ7R2S",
  "databaseURL": "https://wishingwell-7d53a-default-rtdb.firebaseio.com/"
}



firebase=pyrebase.initialize_app(Config)
auth=firebase.auth()
db=firebase.database()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'




#Code goes below here




@app.route('/')
def home():
    return render_template('index.html')



@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass1']
        other_password = request.form['pass2']
        username = request.form['username']
        if password == other_password:
            try:
                login_session['user'] = auth.create_user_with_email_and_password(email, password)
                user = {"username": username, "email": email, "password": password}
                db.child("Users").child(login_session['user']['localId']).set(user)
                return redirect(url_for('home'))
            except:
                print('ERROR')
        else:
            print('not same password')
    return render_template('signup.html')

    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            print(login_session['user']['localId'])
            return redirect(url_for('home'))
        except:
            print('ERROR')
    else: 
        return render_template('login.html')



@app.route('/logout')
def logout():
    if 'user' in login_session:
        login_session['user'] = None
        auth.current_user = None
    return redirect(url_for('home'))



@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        title = request.form['title']
        photo = request.form['photo']
        desc  = request.form['desc']
        username = db.child("Users").child(login_session['user']['localId']).child('username').get().val()
        load = {'title':title, 'photo':photo, 'description':desc}
        # try:
        db.child("Uploads").set(load)


        return redirect(url_for('home'))
    return render_template('upload.html')





@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/cherish')
def cherish():
    return render_template('cherish.html')



@app.route('/card')
def card():
    return render_template('card.html')


#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)