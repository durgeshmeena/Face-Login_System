from flask import Flask,jsonify,request, session, redirect
import uuid
from passlib.hash import pbkdf2_sha256
<<<<<<< Updated upstream
from app import db 
import os
import base64
=======
from app import db, FRmodel
# from app import db

import os
import base64
import numpy as np
from PIL import Image
import base64
import re
from cv2 import cv2
import joblib

>>>>>>> Stashed changes
from user.face_recog import Recog, LoginFaceCapture, SignupFaceCapture

class User:

    def start_session(self, user):
        del user['password']
        session["logged_in"] = True
        session["user"] = user
        return jsonify(user), 200


    def signup(self):
<<<<<<< Updated upstream
        print(request.form)
        SignupFaceCapture().get_frames()
        known_face_encoding = Recog().face_signup()
        if known_face_encoding == 'empty':
            print("not signup")
            return jsonify({"error": "Signup failed"}), 400
     # Create the user object
        user = {
           "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
           "password": request.form.get('password'),
           "face_encoding": known_face_encoding
        }

        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        if db.find_one({"email":user['email']}):
            return jsonify({"error":"Email address already exists"}), 400
    

        if db.insert_one(user):
            return redirect('/user/login')
   
        return jsonify({"error": "Signup failed"}), 400
=======
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
       
>>>>>>> Stashed changes


    def logout(self):
        session.clear()
        return redirect('/')

    
    def login(self):
<<<<<<< Updated upstream
=======
        # name = request.form['name']
        email = request.form['email2']
        password = request.form['password2']
        file = request.form['file2']


>>>>>>> Stashed changes
        user = db.find_one({
            "email": request.form.get('email')
        })
        # print(request)
        # imgURI = request.form.get('imageURI')
        # print(imgURI)
        # rand_name = 'LoginImage' + str(uuid.uuid4())+'.png'
        # if not os.path.exists('uploads/unknown_faces'):
        #     os.makedirs('uploads/unknown_faces')
        # with open("uploads/unknown_faces/"+rand_name, "wb") as fh:
        #     fh.write(base64.decodebytes(imgURI.encode()))
        

        # print(type(user['face_encoding']), user['face_encoding'])
        if user:
<<<<<<< Updated upstream
            if pbkdf2_sha256.verify(request.form.get('password'), user['password']):
                print("here-start")
                LoginFaceCapture().get_frame()
                print("here-end")
                if Recog().face_login(user['face_encoding']):
                    return self.start_session(user)
                return jsonify({"error": "unauthorized access "}), 401
=======
            if pbkdf2_sha256.verify(password, user['password']):
                login_uploaded = Img.save_image(file)
                if login_uploaded:
                    IMG_PATH = 'uploads/user_signup/f.jpg'
                    login_encoding = face_verify.login_img_to_encoding(IMG_PATH, FRmodel)
                    database_encoding = joblib.load(user['database_encoding'][0])
                    if face_verify.verify(login_encoding, database_encoding):
                        return self.start_session(user)
                    return jsonify({"error": "unauthorized access "}), 401
                return jsonify({"error": "Image not uploaded "}), 401    
>>>>>>> Stashed changes
            return jsonify({"error": "Incorrect Password"}), 401
        return jsonify({"error": "Email not registered!!"}), 401

        




        
