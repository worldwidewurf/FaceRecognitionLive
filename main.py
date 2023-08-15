import time
import cv2
import face_recognition
import threading
import faces.loadfaces as lf
import argparse
import faces.registeruser as ru
import faces.removeUser as rmv
import csv

parser = argparse.ArgumentParser(description="Live Facial Recognition And Data Analysis")

parser.add_argument("-ru",type=str,help=" - Register User")
parser.add_argument("-rmv",type=str,help=" - Remove User")

args = parser.parse_args()

latest_frame = None
detected_faces = []
get_name = ["Unknown Person"]

def detect_faces(frame):
    global detected_faces

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    detected_faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

def main():
    global latest_frame, detected_faces,get_name

    cam = cv2.VideoCapture(0)

    

    saved_pictures_face_list = lf.loadpictures()

    def recognition_thread():
        """Thread to recognize faces in the frame
            once a face is detected it will compare it with the saved faces
            and if the face is in the database it will save the attendance entry into a coma separated file csv
            for te first stage of data analysis 
        """
        global latest_frame, detected_faces,get_name

        while True:
            if latest_frame is not None:
                unknown_face_encoding = face_recognition.face_encodings(latest_frame)
                for (name, face_encoding) in saved_pictures_face_list:
                    if len(unknown_face_encoding) > 0:
                        results = face_recognition.compare_faces(face_encoding, unknown_face_encoding[0])
                        if results[0] == True:
                            datetime = time.strftime("%Y-%m-%d %H:%M:%S")
                            with open(f'DataHandling/{time.strftime("%Y-%m-%d")}.csv', 'a', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerow([name, datetime])
                            detected_name = name
                            print("Welcome "+detected_name)
                            get_name.clear()
                            get_name.append(detected_name)
                            time.sleep(10)
                            break
                        else:
                            get_name.clear()
                            detected_name = "Unknown Person"
                            get_name.append(detected_name)
                            print(get_name)


    recognition_thread = threading.Thread(target=recognition_thread)
    recognition_thread.daemon = True
    recognition_thread.start()

    while True:
        ret, frame = cam.read()
        if ret:
            latest_frame = frame.copy()
            detect_faces(latest_frame)
            for (x, y, w, h), name in zip(detected_faces, get_name):
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
    if args.ru:
        ru.register_user(args.ru)
    elif args.rmv:
        rmv.removeUser(args.rmv)
    else:
        main()
