# Facial Recognition using OpenCV and face_recognition

This repository contains a Python script for performing facial recognition using the OpenCV and face_recognition libraries. The script captures video from a webcam, detects faces in the frames, and compares the detected faces with a reference face to determine if they match.

## Requirements

- Python 3.x
- OpenCV (cv2) library
- face_recognition library

You can install the required libraries using the following commands:

```
pip install opencv-python
pip install face-recognition
```
## How to Use
Clone the repository or download the provided script to your local machine.

Make sure you have a working webcam .

Place a reference image named reference.jpg in the same directory as the script. This image will be used to compare detected faces with the reference face.

Open a terminal or command prompt and navigate to the directory containing the script.

Run the script using the following command:

```python liveFaceRecMain.oy```

## Notes
The script uses the Haar Cascade classifier from OpenCV for face detection. Detected faces are highlighted with green rectangles in the webcam feed.


Make sure the reference image (reference.jpg) contains a clear and well-lit image of your face. The success of the recognition depends on the quality of this reference image.

The script's code structure is provided in the script file. If you'd like to understand how it works in more detail, feel free to refer to the script's comments.

## Disclaimer
This script is meant for educational purposes and basic facial recognition demonstrations. Keep in mind that facial recognition technology has broader implications and considerations when used in real-world applications.

