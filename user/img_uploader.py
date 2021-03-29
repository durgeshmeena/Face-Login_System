from flask import Flask, jsonify, request, session, redirect
import uuid
import base64
import os

class Img:
    def upload(self):
        print("recieved here")
        content = request.get_json(force=True)
        self.save_image(content['data'])
        # print(type(content), type(content['data']), '\n', )
        return content

    def save_image(self, b64_string):
        rand_name = 'Image' + str(uuid.uuid4())+'.jpg'
        if not os.path.exists('uploads/known_faces/temp_user'):
            os.makedirs('uploads/known_faces/temp_user')
        with open("uploads/known_faces/temp_user/"+rand_name, "wb") as fh:
            fh.write(base64.decodebytes(b64_string.encode()))
