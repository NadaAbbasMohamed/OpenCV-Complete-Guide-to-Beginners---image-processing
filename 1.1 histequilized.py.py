import numpy as np
import cv2

# loading and converting the image into numpy array
image = cv2.imread('1.2 cat.jpeg.jpeg',1)


# BGR to GRAY
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(gray)
cv2.imshow("Normal and Equilized",np.hstack([gray, eq]))
cv2.waitKey(0)
