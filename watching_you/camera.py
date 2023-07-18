import cv2
def open_camera(cam):
    threat = 0
    while cam.isOpened(): 
        threat += 20
        ret , frame1 = cam.read()
        ret , frame2 = cam.read()
        diff = cv2.absdiff(frame1,frame2)
        gray = cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
        dilate = cv2.dilate(thresh,None,iterations=3)
        contours, _= cv2.findContours(dilate,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(frame1,contours,-1,(0,255,0),2)
        for circle in contours:
            if cv2.contourArea(circle)<5000:
                continue
            x,y,w,h = cv2.boundingRect(circle)
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),3)
            return True
        return False

if __name__ == "__main__":
    open_camera()


