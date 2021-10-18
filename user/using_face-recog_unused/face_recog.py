from flask import Flask, jsonify, request, session, redirect

import face_recognition
import os
from cv2 import cv2
from PIL import Image
import pickle
# import json
import shutil
from bson.binary import Binary
import joblib

class Recog:
    def face_signup(self):
        KNOWN_FACES_DIR = 'uploads/known_faces'

        known_faces = []
        # all_encode = {}
        for name in os.listdir(KNOWN_FACES_DIR):
            for filename in os.listdir(f'{KNOWN_FACES_DIR}/{name}'):
                image = face_recognition.load_image_file(f'{KNOWN_FACES_DIR}/{name}/{filename}')
                encoding = face_recognition.face_encodings(image)
                print(len(encoding),end=" ")
                if len(encoding)>0:
                    encoding= face_recognition.face_encodings(image)[0]
                    print(type(encoding))
                    known_faces.append(encoding)
                else:
                    continue
        
        if not len(known_faces)>0:
            if os.path.exists('uploads/known_faces/signup_user'):
                path = 'uploads/known_faces/signup_user'
                shutil.rmtree(path)
            return "empty"

        
        # print(type(known_faces),known_faces)
        # return known_faces
        # all_encode['face'] = known_faces

        # return Binary(pickle.dumps(all_encode,protocol=2))


        if  os.path.exists('uploads/known_faces/signup_user'):
            path = 'uploads/known_faces/signup_user'
            shutil.rmtree(path)
        return joblib.dump(known_faces, 'known_encodings')
        # return json_data
        # if not os.path.exists('uploads/encoding_files'):
        #     os.makedirs('uploads/encoding_files')

        # with open('uploads/encoding_files/feces_encodings.pickle', 'wb') as f:
        #     pickle.dump(known_faces, f)

    def face_login(self, known_face_encoding):

        UNKNOWN_FACES_DIR = 'uploads/unknown_faces'
        MODEL = 'cnn'
        TOLERANCE = 0.6

        # with open('uploads/encoding_files/feces_encodings.pickle', 'rb') as f:
        #     known_faces=  pickle.load(f)

        known_faces = joblib.load(known_face_encoding[0])
        # print(type(known_face_encoding),type(known_faces), known_faces)
        # return False

        # with open('uploads/encoding_files/Fuckodings.pickle', 'wb') as f:
        #     pickle.dump(known_faces_, f)

        # with open('uploads/encoding_files/Fuckodings.pickle', 'rb') as f:
        #     known_faces =  pickle.load(f)
        
        
        print('Processing unknown faces...')
        for filename in os.listdir(UNKNOWN_FACES_DIR):

            print(f'Filename {filename}', end='')
            image = face_recognition.load_image_file(f'{UNKNOWN_FACES_DIR}/{filename}')
            # locations = face_recognition.face_locations(image, model=MODEL)
            # encodings = face_recognition.face_encodings(image, locations)
            encodings = face_recognition.face_encodings(image)


            # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            print(f', found {len(encodings)} face(s)')

            if len(encodings)==0:
                if os.path.exists('uploads/unknown_faces'):
                    path = 'uploads/unknown_faces'
                    shutil.rmtree(path)
                return False

            for face_encoding in encodings:
                results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
                print(results)
                
                if  os.path.exists('uploads/unknown_faces'):
                    path = 'uploads/unknown_faces'
                    shutil.rmtree(path)

                if True in results:
                    return True
                else:
                    return False
                
            
class LoginFaceCapture:
    def __init__(self):
        print("initialising")
        self.video = cv2.VideoCapture(0)
        print("camera started")

    def get_frame(self):
        for i in range(2):
            sucess, img = self.video.read()
            print('read cam')
            if sucess:
                print("capturing")
                cv2.namedWindow('login_capture')
                cv2.imshow('login_capture', img)
                # cv2.waitKey(0)
                cv2.destroyWindow('login_capture')

                if not os.path.exists('uploads/unknown_faces'):
                    os.makedirs('uploads/unknown_faces')
                if i == 0:
                    cv2.waitKey(2000)
                    continue
                cv2.imwrite('uploads/unknown_faces/login_cap.jpg',img)
                print("done")

                
class SignupFaceCapture:
    def __init__(self):
        print("initialising")
        self.video = cv2.VideoCapture(0)
        print("camera started")

    def get_frames(self):
        for i in range(6):
            sucess, img = self.video.read()
            print('read cam')
            if sucess:
                print("capturing")
                cv2.namedWindow('signup_capture')
                cv2.imshow('signup_capture', img)
                # cv2.waitKey(0)
                cv2.destroyWindow('signup_capture')

                if not os.path.exists('uploads/known_faces/signup_user'):
                    os.makedirs('uploads/known_faces/signup_user')
                if i==0:
                    cv2.waitKey(2000)
                    continue
                cv2.imwrite('uploads/known_faces/signup_user/signup_cap'+str(i)+'.jpg', img)
                cv2.waitKey(1000)

                print("done")


# mns = SignupFaceCapture()
# mns.get_frames()
