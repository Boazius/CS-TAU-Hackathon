from flask import Flask, request, jsonify
from imageai.Detection import ObjectDetection
import os
import io
import time
from PIL import Image

app = Flask(__name__)

class ObjectDetectionModel:
    def __init__(self):
        self.execution_path = os.getcwd()
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsTinyYOLOv3()
        self.detector.setModelPath(os.path.join(self.execution_path, "tiny-yolov3.pt"))
        self.detector.loadModel()

    def detect_objects(self, image_data, object_name):
        # Save the image to an in-memory file
        image = Image.open(io.BytesIO(image_data))
        temp_file_path = os.path.join(self.execution_path, 'temp.jpg')
        image.save(temp_file_path)
        
        custom_objects = self.detector.CustomObjects(**{object_name: True})
        start_time = time.time()
        detections = self.detector.detectObjectsFromImage(
            custom_objects=custom_objects,
            input_image=temp_file_path,
            output_image_path=os.path.join(self.execution_path, "detected_image.jpg"),
            minimum_percentage_probability=30
        )
        detection_time = time.time() - start_time
        detected_objects = {eachObject["name"] for eachObject in detections}
        return object_name in detected_objects, detection_time

# Initialize the model once
model = ObjectDetectionModel()

@app.route('/detect', methods=['POST'])
def detect():
    if 'object_name' not in request.form or 'image' not in request.files:
        return jsonify({"error": "Missing object_name or image"}), 400

    object_name = request.form['object_name']
    image_file = request.files['image']
    image_data = image_file.read()
    
    detected, detection_time = model.detect_objects(image_data, object_name)
    response = {
        'detected': detected,
        'detection_time': detection_time
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
