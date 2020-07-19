# Cats-Vs-Dogs-Flask-webapp
This project is a part of Coursera's Guided Project - [ Deploy Models with TensorFlow Serving and Flask ](https://www.coursera.org/learn/deploy-models-tensorflow-serving-flask)

It serves as a very basic introduction for deploying TF models using TensorFlow Serving, Docker and creating a simple web app with FLASK.


# Steps to follow

1) Create a directory named ```static```. This is required as the input image for the model will be saved here when you run ```app.py```. By default FLASK will read the image from ```static``` directory.
2) Install the python packages required:

    ```pip3 install tensorflow==2.1.0 flask flask-bootstrap requests```
3) Launch the docker instance which will serve the TensorFlow SavedModel (in the pets folder):

    ```sudo docker run -p PORT_NUMBER:8501 --name=pets -v "YOUR_SAVED_MODEL_PATH:/models/pets/1" -e MODEL_NAME=pets tensorflow/serving```

    In the project, we used 8502 for the ```PORT_NUMBER``` , and ```YOUR_SAVED_MODEL_PATH``` needs to be the absolute path of the pets folder in your
    local machine. So, if you extracted the downloaded zip file in, say, ```/home/example/``` , and want to use 8502 for the server port, the above
    command will become:

    ```sudo docker run -p 8502:8501 --name=pets -v "/home/example/pets/:/models/pets/1" -e MODEL_NAME=pets tensorflow/serving```

    Please note if you use any other port, you will have to change the MODEL_URL in the app.py file accordingly



4) Now run  ```python3 app.py``` and visit the link shown in Terminal/Command Prompt.
