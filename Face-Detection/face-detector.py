import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('test2.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray , 1.1 , 4)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y) , (x+w , y+h) , (225, 0 , 0) , 3)

cv2.imshow('img' , img)
cv2.waitKey()

cv2.imwrite("after_face_detect2.jpg" , img)