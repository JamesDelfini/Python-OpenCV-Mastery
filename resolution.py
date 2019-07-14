## Remain the comment configuration below for pylint source-code, bug and quality checker.
# pylint: disable=maybe-no-member

from core.general import showMsg
import cv2

###################################
## Description: Image Shape Information
###################################
# Black and White (Grayscale)
# PictureDimension 1920x1200 
# 1920 Width Pixels x 1200 Height Pixels
img = cv2.imread("Images/Black Clover.png", 1)
showMsg(img.shape)
# (1200, 1920)
# 1200 rows (img.shape[0])
# 1920 columns  (img.shape[1])
# x(n) of channel (img.shape[2]) - This is only shown for colored imaged  

# showMsg(img.shape[0])

###################################
## Description: Display Image
# cv2.imshow(<Windows Name>, <image>)
# @param image - Requires cv2.imread()
###################################
cv2.imshow("Original Size Black Clover 1920x1200", img)
cv2.waitKey(0) 
cv2.destroyAllWindows() # Destroys all the windows that are created
# cv2.destroyWindow() # Special case where you can already create a window and load image to it 

###################################
## Description: Resizing Image
# cv2.resize(<image>, )
# @param image - Requires cv2.imread()
###################################
resized_image = cv2.resize(img, (500, 500))
cv2.imshow("Resized Image Black Clover 500x500", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

resized_image = cv2.resize(img, ((int(img.shape[1]/2)), int(img.shape[0]/2)) )
cv2.imshow("Resized Image Black Clover 500x500", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()