from flask import Flask,jsonify,request, session, redirect
import uuid
from passlib.hash import pbkdf2_sha256
from app import db 
import os
import base64
from user.face_recog import Recog, LoginFaceCapture, SignupFaceCapture

class User:

    def start_session(self, user):
        del user['password']
        session["logged_in"] = True
        session["user"] = user
        return jsonify(user), 200


    def signup(self):
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


    def logout(self):
        session.clear()
        return redirect('/')

    
    def login(self):
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
            if pbkdf2_sha256.verify(request.form.get('password'), user['password']):
                print("here-start")
                LoginFaceCapture().get_frame()
                print("here-end")
                if Recog().face_login(user['face_encoding']):
                    return self.start_session(user)
                return jsonify({"error": "unauthorized access "}), 401
            return jsonify({"error": "Incorrect Password"}), 401
        return jsonify({"error": "Email not registered!!"}), 401

        




        
