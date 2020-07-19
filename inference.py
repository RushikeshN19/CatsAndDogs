import tensorflow as tf
import numpy as np
import json
import requests

SIZE=128
MODEL_URL = 'http://localhost:8501/v1/models/pets:predict'
CLASS_LABELS = ['Cat', 'Dog']

def get_prediction(image_path):
    image = tf.keras.preprocessing.image.load_img(
        image_path, target_size= (SIZE,SIZE)
    )
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    image = np.expand_dims(image, axis=0)

    # create a json object to be sent to the server
    data = json.dumps({
        'instances': image.tolist()
    })
    response = requests.post(MODEL_URL, data=data.encode())
    result= json.loads(response.text)
    # print(result)
    prediction = np.squeeze(result['predictions'][0])
    class_name = CLASS_LABELS[int(prediction>0.5)]
    return class_name
