import base64
import os
import numpy as np
import cv2
import mtcnn

class Img:
    def save_image(file):
        image_b64 = file.split(",")[1]
        binary = base64.b64decode(image_b64)
        image = np.asarray(bytearray(binary), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        detector = mtcnn.MTCNN()
        result = detector.detect_faces(image)
        if result:
            # extract the bounding box from the first face
            x1, y1, width, height = result[0]['box']
            # bug fix
            x1, y1 = abs(x1), abs(y1)
            x2, y2 = x1 + width, y1 + height
            face = image[y1:y2, x1:x2]

            IMG_PATH = 'uploads/user_signup/a.jpg' 
            cv2.imwrite(IMG_PATH, image)

            IMG_PATH = 'uploads/user_signup/f.jpg' 
            status = cv2.imwrite(IMG_PATH, face)   
            if status:
                return True
            return False   
        else:
            return False    
        
        
        
