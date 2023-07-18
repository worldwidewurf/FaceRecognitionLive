import threading
import cv2
from deepface import DeepFace
from watching_you import camera as detect
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False

referenceImage = cv2.imread('reference.jpg')

def check_face(frame):
    global face_match
    try:
        if frame is not None:
            if DeepFace.verify(frame, referenceImage.copy())["verified"]:
                face_match = True
            else:
                face_match = False
        else:
            
            face_match = False
    except ValueError:
        face_match = False

while True:
    ret, frame = cap.read()
    cv2.imshow("Frame", frame)
    if ret == True:  
        if detect.open_camera(cap):
            try:
                threading.Thread(target=check_face(frame), args=(frame,)).start()
            except ValueError:
                pass

        if face_match:
            print("Face Matched")
            cv2.putText(frame, "Face Matched", (20, 450), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
        else:
            print("Face Not Matched")
            cv2.putText(frame, "Face Not Matched", (20, 450), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)
        
        print("sdfghj")
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
