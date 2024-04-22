import json

import numpy as np

import os

from keras.preprocessing import image
from tensorflow import keras
from flask import Flask, request
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app, supports_credentials=True)



@app.route('/')
def main():
    return "You are on the main page"


@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':

        if 'file' not in request.files:
            print('No file part')

        uploaded_file = request.files['file']
        if uploaded_file:
            filename = secure_filename(uploaded_file.filename)
            uploaded_file.save(filename)

            if uploaded_file.filename != '':

                model = keras.models.load_model("model_unoptimized.h5")
                fileProcessed = uploaded_file.filename

                normal = image.image_utils.load_img(fileProcessed, target_size=(224, 224))

                img_tensor = image.image_utils.img_to_array(normal)
                img_tensor = np.expand_dims(img_tensor, axis=0)
                img_tensor /= 255.

                pred = model.predict(img_tensor)[0]

                maximumValue = 0
                maximumIndex = 0
                index = 0
                while index < len(pred):
                    if pred[index] > maximumValue:
                        maximumValue = pred[index]
                        maximumIndex = index

                    index += 1
                percentage = maximumValue * 100
                res = {
                    "Prediction": "unknown",
                    "Probability": str(percentage) + "%"
                }

                if maximumIndex == 0:
                    res['Prediction'] = 'Adenocarcinoma'
                if maximumIndex == 1:
                    res['Prediction'] = 'Large Cell Carcinoma'
                if (maximumIndex == 2):
                    res['Prediction'] = 'No Tumor'
                if (maximumIndex == 3):
                    res['Prediction'] = 'Squamous Cell Carcinoma'
                os.remove(uploaded_file.filename)
                return json.dumps(res)
        else:
            return 'Error'


app.run(host='localhost', port=5000)
