from flask import Flask, jsonify, request, session, redirect
import uuid
import base64
import os

class Img:
<<<<<<< Updated upstream
    def upload(self):
        print("recieved here")
        content = request.get_json(force=True)
        self.save_image(content['data'])
        # print(type(content), type(content['data']), '\n', )
        return content
=======
    def save_image(file):
        image_b64 = file.split(",")[1]
        binary = base64.b64decode(image_b64)
        image = np.asarray(bytearray(binary), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
>>>>>>> Stashed changes

    def save_image(self, b64_string):
        rand_name = 'Image' + str(uuid.uuid4())+'.jpg'
        if not os.path.exists('uploads/known_faces/temp_user'):
            os.makedirs('uploads/known_faces/temp_user')
        with open("uploads/known_faces/temp_user/"+rand_name, "wb") as fh:
            fh.write(base64.decodebytes(b64_string.encode()))
