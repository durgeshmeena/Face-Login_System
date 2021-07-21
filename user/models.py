from flask import Flask,jsonify,request, session, redirect
import uuid
from passlib.hash import pbkdf2_sha256
import joblib

from user.img_uploader import Img
from user import face_verify 
from app import db, FRmodel


class User:

    def start_session(self, user):
        del user['password']
        session["logged_in"] = True
        session["user"] = user
        return jsonify(user), 200

    def signup(self):
        # data = [request.form['name'], request.form['email'], request.form['password'] ]
        
        file = request.form['file']
        
        image_uploaded = Img.save_image(file)
        # print(image_upload)
        if image_uploaded:
            IMG_PATH = 'uploads/user_signup/f.jpg'
            img_encoding = face_verify.img_to_encoding(IMG_PATH, FRmodel)
        else:
            return jsonify({"error": "Signup failed"}), 400 
        # print(img_encoding)

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        print(name, email, password)
        # print(img_encoding)

        if len(img_encoding):
            user = {
                "_id": uuid.uuid4().hex,
                "name": request.form.get('name'),
                "email": request.form.get('email'),
                "password": request.form.get('password'),
                "database_encoding": img_encoding
            }

            user['password'] = pbkdf2_sha256.encrypt(user['password'])

            if db.find_one({"email":user['email']}):
                return jsonify({"error":"Email address already exists"}), 400

            if db.insert_one(user):
                return jsonify({"sucess": "Signup sucessfully"}), 200

        return jsonify({"error": "Signup failed"}), 400    
       


    def logout(self):
        session.clear()
        return redirect('/')

    
    def login(self):
        # name = request.form['name']
        email = request.form['email2']
        password = request.form['password2']
        file = request.form['file2']


        user = db.find_one({
            "email": email
        })

        if user:
            if pbkdf2_sha256.verify(password, user['password']):
                login_uploaded = Img.save_image(file)
                if login_uploaded:
                    IMG_PATH = 'uploads/user_signup/f.jpg'
                    login_encoding = face_verify.login_img_to_encoding(IMG_PATH, FRmodel)
                    database_encoding = joblib.load(user['database_encoding'][0])
                    if face_verify.verify(login_encoding, database_encoding):
                        return self.start_session(user)
                    return jsonify({"error": "Unauthorized access "}), 401
                return jsonify({"error": "Face not found "}), 401    
            return jsonify({"error": "Incorrect Password"}), 401
        return jsonify({"error": "Email not registered!!"}), 401

    def login_recog(self):
        file = request.form['file3']  
        login_recog_uploaded = Img.save_image(file)
        if login_recog_uploaded:
                    IMG_PATH = 'uploads/user_signup/f.jpg'
                    login_recog_encoding = face_verify.login_img_to_encoding(IMG_PATH, FRmodel)

                    data = db.find()
                    print("data= ", data)
                    for user in data:
                        print(user['name'],user['database_encoding'][0])
                        database_encoding = joblib.load(user['database_encoding'][0])
                        if face_verify.verify(login_recog_encoding, database_encoding):
                            return self.start_session(user)

                    return jsonify({"error": "unauthorized access "}), 401
        return jsonify({"error": "Face not found "}), 401 





        
