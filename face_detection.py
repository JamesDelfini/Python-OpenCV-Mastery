## Remain the comment configuration below for pylint source-code, bug and quality checker.
# pylint: disable=maybe-no-member

from core.general import showMsg
import cv2

# Creating a CascadeClassifierObject
face_cascade = cv2.CascadeClassifier("classifier/predefined/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("classifier/predefined/haarcascade_eye.xml")

# Reading the image
img = cv2.imread("images/MeMyselfAndI2.jpg")
# Reading the image as gray scae Image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Search the coordinates of the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors = 30)

print(type(faces))
print(faces)

for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
    roi_gray = gray_img[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)

    print(type(eyes))
    print(eyes)

    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)
        
cv2.imshow('Face Detection',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

####################################
## Description: CascadeClassifier::detectMultiScale
# Detects objects of different sizes in the input image. The detected objects are returned as a list of rectangles. 
# cv2.CascadeClassifier::detectMultiScale(<image>, [<object>], [<scaleFactor>], [<minNeighbors>], [<flags>], [<minSize>], [<maxSize>])
#
# Image - Matrix of the type CV_8U containing an image where objects are detected. 
# Cascade Classifier must be in xml and it is created by training by using Haar Cascade. 
#
## Link Reference: https://docs.opencv.org/4.1.0/d1/de5/classcv_1_1CascadeClassifier.html
###################################

###################################
## Description: Rectangle
# cv2.rectangle(<image>, <flag>)
#
## Drawing Rectangle
# To draw a rectangle, you need top-left corner and bottom-right corner of rectangle. 
# This time we will draw a green rectangle at the top-right corner of image. 
# e.g. cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,0), 1)
#
## Drawing Circle
# To draw a circle, you need its center coordinates and radius. 
# We will draw a circle inside the rectangle drawn above. 
# e.g. cv2.circle(img,(447,63), 63, (0,0,255), -1)
#
## Drawing Ellipse
# To draw the ellipse, we need to pass several arguments. 
# One argument is the center location (x,y). 
# Next argument is axes lengths (major axis length, minor axis length). 
# angle is the angle of rotation of ellipse in anti-clockwise direction. 
# startAngle and endAngle denotes the starting and ending of ellipse 
# arc measured in clockwise direction from major axis. i.e. giving 
# values 0 and 360 gives the full ellipse. For more details, check 
# the documentation of cv2.ellipse(). Below example draws a 
# half ellipse at the center of the image. 
# e.g. cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
#
## Drawing Polygon
# To draw a polygon, first you need coordinates of vertices. 
# Make those points into an array of shape ROWSx1x2 where ROWS are 
# number of vertices and it should be of type int32. 
# Here we draw a small polygon of with four vertices in yellow color. 
# e.g. ...
# pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# pts = pts.reshape((-1,1,2))
# cv2.polylines(img,[pts],True,(0,255,255))
#
## Adding Text to Images:
# To put texts in images, you need specify following things.
# Text data that you want to write
# Position coordinates of where you want put it (i.e. bottom-left corner where data starts). 
# Font type (Check cv2.putText() docs for supported fonts)
# Font Scale (specifies the size of font)
# regular things like color, thickness, lineType etc. For better look, lineType = cv2.LINE_AA is recommended.
# e.g. ...
# We will write OpenCV on our image in white color. 
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
#
## Link Reference 
# https://docs.opencv.org/3.1.0/dc/da5/tutorial_py_drawing_functions.html
###################################

# Example Drawing a Rectangle
# x1,y1 ------
# |          |
# |          |
# |          |
# --------x2,y2