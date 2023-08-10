import cv2
import face_recognition
import threading
import faces.loadfaces as lf

latest_frame = None
detected_faces = []

def detect_faces(frame):
    global detected_faces

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    detected_faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

def main():
    global latest_frame, detected_faces

    cam = cv2.VideoCapture(0)

    

    saved_pictures_face_list = lf.loadpictures()

    def recognition_thread():
        global latest_frame, detected_faces

        while True:
            if latest_frame is not None:
                unknown_face_encoding = face_recognition.face_encodings(latest_frame)
                for (name, face_encoding) in saved_pictures_face_list:
                    if len(unknown_face_encoding) > 0:
                        results = face_recognition.compare_faces(face_encoding, unknown_face_encoding[0])
                        if results[0] == True:
                            detected_name = name
                            # print(results)
                        else:
                            detected_name = "Unknown Person"
                        
                        

    recognition_thread = threading.Thread(target=recognition_thread)
    recognition_thread.daemon = True
    recognition_thread.start()

    while True:
        ret, frame = cam.read()
        if ret:
            latest_frame = frame.copy()
            detect_faces(latest_frame)
            for (x, y, w, h), (name, _) in zip(detected_faces, saved_pictures_face_list):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            cv2.imshow("Facial Recognition <(-|-)>", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
