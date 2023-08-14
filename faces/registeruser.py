import os
import cv2

def detect_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
    return faces

def register_user(username):
    """Register a user by taking a picture of the user and saving it in the images folder

    Args:
        username (str): The name/username of the user to be registered
    """
    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()
        if not ret:
            break
        
        faces = detect_face(frame)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            img = frame.copy()

        cv2.imshow("Register User", frame)
        
        key = cv2.waitKey(1)
        if key == ord('s') and len(faces) > 0:            
            
            filename = "faces/images/" +username+".jpg"
            
            if os.path.exists(filename):
                print("User already exists")
                break
            cv2.imwrite(filename, img)
        if key == 27: 
            break

    cam.release()
    cv2.destroyAllWindows()
