import cv2

#xml that is necessary for face detection is imported 

face_cascade=cv2.CascadeClassifier('E:\opencv\haarcascade_frontalface_default.xml')


img=cv2.imread('E:\opencv\hello.JPG')



gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray,1.1,4)



for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


cv2.imshow("img",img)
cv2.waitKey()
    