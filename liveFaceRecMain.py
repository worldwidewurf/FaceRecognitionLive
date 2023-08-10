import cv2
import face_recognition
import threading

# Global variables to store the latest webcam frame and detected faces
latest_frame = None
detected_faces = []

def detect_faces(frame):
    global detected_faces

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    detected_faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

def main():
    global latest_frame, detected_faces

    cam = cv2.VideoCapture(0)

    picture_of_me = face_recognition.load_image_file("reference.jpg")
    my_face_encoding = face_recognition.face_encodings(picture_of_me)

    if len(my_face_encoding) == 0:
        print("No face found in the reference image!")
        return

    def recognition_thread():
        global latest_frame, detected_faces

        while True:
            if latest_frame is not None:
                unknown_face_encoding = face_recognition.face_encodings(latest_frame)
                
                if len(unknown_face_encoding) > 0:
                    results = face_recognition.compare_faces(my_face_encoding, unknown_face_encoding[0])
                    if results[0] == True:
                        print("It's a picture of me!")
                    else:
                        print("It's not a picture of me!")

    recognition_thread = threading.Thread(target=recognition_thread)
    recognition_thread.daemon = True
    recognition_thread.start()

    while True:
        ret, frame = cam.read()
        if ret:
            latest_frame = frame.copy()
            detect_faces(latest_frame)
            for (x, y, w, h) in detected_faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

            cv2.imshow("Facial Recognition <(-|-)>", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
