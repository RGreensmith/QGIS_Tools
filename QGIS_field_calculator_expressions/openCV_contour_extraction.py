import cv2
import numpy as np 
img = cv2.imread('./test_images/central.jpg')  #read image from system
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #Convert to grayscale image
edged = cv2.Canny(gray, 170, 255)            #Determine edges of objects in an image
ret,thresh = cv2.threshold(gray,240,255,cv2.THRESH_BINARY)  
(contours,_) = cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #Find contours in an image

for cnt in contours:
    cv2.drawContours(img,[cnt],-1,(0,255,0),2)
    cv2.imshow('polygons_detected',img) 
cv2.waitKey(0) 
cv2.destroyAllWindows()