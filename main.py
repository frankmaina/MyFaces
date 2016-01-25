import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haar.xml')


img = cv2.imread('image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray, 1.07, 8)
count = 0
for (x,y,w,h) in faces:
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
	count += 1
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = img[y:y+h, x:x+w]

print count
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()