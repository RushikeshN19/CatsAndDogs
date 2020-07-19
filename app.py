from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
import os
import inference
app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method =='POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename.endswith('.jpg') or uploaded_file.filename.endswith('.png') or uploaded_file.filename.endswith('.jpeg'):
            image_path = os.path.join('static', uploaded_file.filename)
            uploaded_file.save(image_path)
            class_name = inference.get_prediction(image_path)

            result = {
            'class_name':class_name,
            'image_path': image_path
            }
            return render_template('show.html', result=result)
    return render_template('index.html') # by default it will look in templates folder

if __name__ == '__main__':
    app.run(debug=True)
