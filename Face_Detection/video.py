import cv2

#xml that is necessary for face detection is imported 

face_cascade=cv2.CascadeClassifier('E:\opencv\haarcascade_frontalface_default.xml')


cap=cv2.VideoCapture(0)

#0 define that video is being taken from web cam , if you want to detect ffrom some .mp4 gives its path

while True:
    flag,img=cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2 reads only gray and typical rgb as bgr (color) 

    faces=face_cascade.detectMultiScale(gray,1.1,4)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    
    
    cv2.imshow("img",img)

    p=cv2.waitKey(30) & 0xff
    
    # waiting for escape key to break
    if p==27:
        break

cap.release()
    




    