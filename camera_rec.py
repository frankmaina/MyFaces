import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haar.xml')
if face_cascade.empty(): raise Exception("your face_cascade is empty. are you sure, the path is correct ?")

video = cv2.VideoCapture(0)
while(video.isOpened()):
	ret, frame = video.read()
	if frame is not None:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 8)
		for (x,y,w,h) in faces:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(118,238,0),2)
			font = cv2.FONT_HERSHEY_SIMPLEX
			cv2.putText(frame,'FACE',(x+10,y+30), font, 0.5,(118,238,0),2,cv2.LINE_AA)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = frame[y:y+h, x:x+w]
		cv2.imshow('Video', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
	    break

video.release()
cv2.destroyAllWindows()