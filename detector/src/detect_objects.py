from imageai.Detection import ObjectDetection
import os
import time

class ObjectDetectionModel:
    def __init__(self, object_names):
        self.execution_path = os.getcwd()
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsTinyYOLOv3()
        self.detector.setModelPath(os.path.join(self.execution_path, "tiny-yolov3.pt"))
        self.detector.loadModel()
        self.custom_objects = self.detector.CustomObjects(**{name: True for name in object_names})

    def detect_objects(self, image_path):
        start_time = time.time()
        detections = self.detector.detectObjectsFromImage(
            custom_objects=self.custom_objects,
            input_image=image_path,
            output_image_path=os.path.join(self.execution_path, "detected_image.jpg"),
            minimum_percentage_probability=30
        )
        detection_time = time.time() - start_time
        detected_objects = {eachObject["name"] for eachObject in detections}
        return detected_objects, detection_time

# Example usage:
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python detect_objects.py <image_path> <object_name_1> [<object_name_2> ...]")
    else:
        image_path = sys.argv[1]
        object_names = sys.argv[2:]
        model = ObjectDetectionModel(object_names)
        results, detection_time = model.detect_objects(image_path)
        detection_results = {name: (name in results) for name in object_names}
        print(f"Detection Results: {detection_results}")
        print(f"Detection Time: {detection_time} seconds")
