from imageai.Detection import ObjectDetection
import os
import sys

def detect_object(image_path, object_name):
    # Get the current working directory
    execution_path = os.getcwd()

    # Initialize the ObjectDetection object
    detector = ObjectDetection()
    
    # Set model type to TinyYOLOv3
    detector.setModelTypeAsTinyYOLOv3()
    
    # Set model path to the downloaded TinyYOLOv3 model
    detector.setModelPath(os.path.join(execution_path, "tiny-yolov3.pt"))
    
    # Load the model
    detector.loadModel()

    # Set custom objects for detection
    custom_objects = detector.CustomObjects(**{object_name: True})
    
    # Perform object detection
    detections = detector.detectObjectsFromImage(
        custom_objects=custom_objects,
        input_image=image_path,
        output_image_path=os.path.join(execution_path, "detected_image.jpg"),
        minimum_percentage_probability=30
    )

    # Check if the specified object is detected
    for eachObject in detections:
        if eachObject["name"] == object_name:
            return "yes"
    return "no"

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python detect_objects.py <image_path> <object_name>")
    else:
        # Get image path and object name from command line arguments
        image_path = sys.argv[1]
        object_name = sys.argv[2]
        
        # Run the object detection
        result = detect_object(image_path, object_name)
        
        # Print the result
        print(result)
