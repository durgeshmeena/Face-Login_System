from flask import Flask, render_template
from app import app
from user.models import User
from user.img_uploader import Img

@app.route('/user/signup', methods=["POST"])
def signup():
    return User().signup()

@app.route('/user/logout')
def logout():
    return User().logout()


@app.route('/user/login', methods=["POST"])
def login():
    return User().login()

@app.route('/user/login-recog', methods=['POST'])
def login_recog():
    return User().login_recog()

@app.route('/user/signup', methods=["GET"])
def signup_get():
    return render_template("signup.html")


@app.route('/user/login', methods=["GET"])
def login_get():
    return render_template("login.html")

@app.route('/user/login-recog', methods=['GET'])
def login_recog_get():
    return render_template('login_recog.html')

# @app.route('/user/upload', methods=['POST'])
# def img_upload():
#     return Img().upload()
