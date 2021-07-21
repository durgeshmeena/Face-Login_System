import tensorflow as tf
import numpy as np
import joblib




def load_model():
    model_path = "tf_files/keras-facenet-tf23"
    model = tf.keras.models.load_model(model_path)
    model.load_weights('tf_files/keras-facenet-h5/model.h5')
    return model

def img_to_encoding(image_path, model):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(160, 160))
    img = np.around(np.array(img) / 255.0, decimals=12)
    x_train = np.expand_dims(img, axis=0)
    embedding = model.predict_on_batch(x_train)
    data = embedding / np.linalg.norm(embedding, ord=2)
    return joblib.dump(data, 'known_encodings')

def login_img_to_encoding(image_path, model):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(160, 160))
    img = np.around(np.array(img) / 255.0, decimals=12)
    x_train = np.expand_dims(img, axis=0)
    embedding = model.predict_on_batch(x_train)
    return embedding / np.linalg.norm(embedding, ord=2)
       

# print(img_to_encoding('uploads/user_signup/a.jpg', FRmodel))
# print(img_to_encoding('src/1.jpg', FRmodel))

def verify(login_encoding, database_encoding):
    # login_encoding = img_to_encoding(image_path, model)
    dist = np.linalg.norm(database_encoding - login_encoding)
    if dist < 0.7:
        return True
    else:
        return False



def identify(image_path, database, model):


    encoding =  img_to_encoding(image_path, model)
    
    
    min_dist = 100
    
    for (name, db_enc) in database.items():
        
        dist = np.linalg.norm(db_enc - encoding)

        if dist<min_dist:
            min_dist = dist
            identity = name
    
    if min_dist > 0.7:
        print("Not in the database.")
    else:
        print ("it's " + str(identity) + ", the distance is " + str(min_dist))
        
    return min_dist, identity