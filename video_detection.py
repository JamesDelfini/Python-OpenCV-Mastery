## Remain the comment configuration below for pylint source-code, bug and quality checker.
# pylint: disable=maybe-no-member
import cv2, time

#####################################
## Description: Capturing a Video First Frame
##################################### 
# video = cv2.VideoCapture(0)
# check, frame = video.read()

# print(check)
# print(frame)

# time.sleep(3)

# cv2.imshow('Capture First Frame', frame)

# cv2.waitKey(0)
# video.release()

# cv2.destroyAllWindows()

#####################################
## Description: Capturing a Video
##################################### 
# Open Video
video = cv2.VideoCapture(0)

numFrames = 1 

# Face Detection
face_cascade = cv2.CascadeClassifier('classifier/predefined/haarcascade_frontalface_default.xml')

while True:
    numFrames += 1
    check, frame = video.read()
    grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grayImg, scaleFactor = 1.05, minNeighbors = 30)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(grayImg, (x, y), (x+w, y+h), (255, 0, 0), 1)

    cv2.imshow('Capturing', grayImg)

    key = cv2.waitKey(1)

    if key == ord('q'): # Once you enter "q" the window will be destroyed
        break

print(numFrames) # This will print the number of frames captured
video.release()
cv2.destroyAllWindows()