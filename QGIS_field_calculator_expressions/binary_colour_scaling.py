import cv2
  
originalImage = cv2.imread('./test_images/central.jpg')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
  
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
 
cv2.imwrite('./test_images/centralBW.jpg',blackAndWhiteImage)
