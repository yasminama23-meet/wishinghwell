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
def homear():
    return render_template('indexar.html')



@app.route('/signup', methods=['GET','POST'])
def signupar():
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
                return redirect(url_for('homear'))
            except:
                print('ERROR')
        else:
            print('not same password')
    return render_template('signupar.html')

    

@app.route('/login', methods=['GET', 'POST'])
def loginar():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            print(login_session['user']['localId'])
            return redirect(url_for('homear'))
        except:
            print('ERROR')
    else: 
        return render_template('loginar.html')



@app.route('/logout')
def logoutar():
    if 'user' in login_session:
        login_session['user'] = None
        auth.current_user = None
    return redirect(url_for('homear'))



@app.route('/upload', methods=['GET', 'POST'])
def upload_imagear():
    if request.method == 'POST':
        title = request.form['title']
        photo = request.form['photo']
        desc  = request.form['desc']
        username = db.child("Users").child(login_session['user']['localId']).child('username').get().val()
        load = {'title':title, 'photo':photo, 'description':desc, 'user':username}
        db.child("Uploads").push(load)
        return redirect(url_for('postsar'))
    return render_template('uploadar.html')


@app.route('/posts')
def postsar():
    total_posts = db.child('Uploads').get().val()
    total_names = total_posts.keys()
    return render_template('postsar.html', names=total_names, posts=total_posts)




@app.route('/about')
def aboutar():
    return render_template('aboutar.html')



@app.route('/cherish')
def cherishar():
    return render_template('cherishar.html')



@app.route('/card')
def cardar():
    return render_template('cardar.html')


#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)