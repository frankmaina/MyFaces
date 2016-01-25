import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haar.xml')


img = cv2.imread('image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray,  scaleFactor=1.1,
    minNeighbors=6,
    minSize=(30, 30),
    flags=0)
count = 0
for (x,y,w,h) in faces:
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
	count += 1
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img,'FACE: '+str(count),(x+10,y+30), font, 0.5,(0,254,0),2,cv2.LINE_AA)
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = img[y:y+h, x:x+w]

print count
cv2.imshow('img',img)
cv2.imwrite( "faces_detected.jpg", img );
cv2.waitKey(0)
cv2.destroyAllWindows()