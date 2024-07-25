from flask import Flask, request, jsonify
from imageai.Detection import ObjectDetection
import os
import time

app = Flask(__name__)

class ObjectDetectionModel:
    def __init__(self):
        self.execution_path = os.getcwd()
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsTinyYOLOv3()
        self.detector.setModelPath(os.path.join(self.execution_path, "tiny-yolov3.pt"))
        self.detector.loadModel()

    def detect_objects(self, image_path, object_name):
        custom_objects = self.detector.CustomObjects(**{object_name: True})
        start_time = time.time()
        detections = self.detector.detectObjectsFromImage(
            custom_objects=custom_objects,
            input_image=image_path,
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
    file = request.files['image']
    image_path = os.path.join(model.execution_path, 'temp.jpg')
    file.save(image_path)
    
    detected, detection_time = model.detect_objects(image_path, object_name)
    response = {
        'detected': detected,
        'detection_time': detection_time
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
