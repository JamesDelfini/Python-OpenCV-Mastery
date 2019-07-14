## Remain the comment configuration below for pylint source-code, bug and quality checker.
# pylint: disable=maybe-no-member
import cv2
import imutils
import numpy
import time
import datetime

from imutils.video import FPS

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('classifier/predefined/haarcascade_frontalface_default.xml')

time.sleep(1.0)

fps = FPS().start()

# start = datetime.datetime.now()
# end = None
numFrames = 0

while True:
    check, frame = video.read()

    if check:
        # end = datetime.datetime.now()

        frame = imutils.resize(frame, width=450)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = numpy.dstack([frame, frame, frame])

        # cv2.putText(frame, "FPS: {}".format(numFrames/(end - start).total_seconds()), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.putText(frame, "Frames: {}".format(numFrames), (10, 30), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        faces = face_cascade.detectMultiScale(frame, scaleFactor = 1.05, minNeighbors = 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 1)	

        cv2.imshow('Video', frame)
        fps.update()
        numFrames += 1
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    else:
        print("[INFO] No video device found")
        break

fps.stop()
video.release()
cv2.destroyAllWindows()

print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
