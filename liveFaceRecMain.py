import cv2
import face_recognition


def detect_face(cam):

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    while cam.isOpened():
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
        cv2.imshow("Facial Recognition <(-|-)>", frame)
        
        if len(faces) > 0:

            return True,frame

        return False,frame

def main():
    cam = cv2.VideoCapture(0)

    picture_of_me = face_recognition.load_image_file("reference.jpg")
    my_face_encoding = face_recognition.face_encodings(picture_of_me)

    if len(my_face_encoding) == 0:
        print("No face found in the reference image!")
        return

    while True:
        face, frame = detect_face(cam)
        if not face:
            print("No face found in the webcam")
            continue

        unknown_face_encoding = face_recognition.face_encodings(frame)

        if len(unknown_face_encoding) == 0:
            print("No face found in the webcam!")
            continue

        results = face_recognition.compare_faces(my_face_encoding, unknown_face_encoding[0])

        if results[0] == True:
            print("It's a picture of me!")
        else:
            print("It's not a picture of me!")

        if cv2.waitKey(1) & 0xFF == ord('q'):  
            break

    cam.release()
    cv2.destroyAllWindows()


main()