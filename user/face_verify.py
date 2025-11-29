import tensorflow as tf
import numpy as np
import joblib




def load_model():
    # Load model using TFSMLayer for Keras 3
    model = tf.keras.layers.TFSMLayer('tf_files/keras-facenet-tf23', call_endpoint='serving_default')
    return model

def img_to_encoding(image_path, model):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(160, 160))
    img = np.around(np.array(img) / 255.0, decimals=12)
    x_train = np.expand_dims(img, axis=0)
    # TFSMLayer returns a dict, extract the output
    result = model(x_train)
    # Try to extract the first output value from the dict
    if isinstance(result, dict):
        embedding = list(result.values())[0]
    else:
        embedding = result
    data = embedding / np.linalg.norm(embedding, ord=2)
    return joblib.dump(data, 'known_encodings')

def login_img_to_encoding(image_path, model):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(160, 160))
    img = np.around(np.array(img) / 255.0, decimals=12)
    x_train = np.expand_dims(img, axis=0)
    # TFSMLayer returns a dict, extract the output
    result = model(x_train)
    if isinstance(result, dict):
        embedding = list(result.values())[0]
    else:
        embedding = result
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