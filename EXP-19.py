import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\tejv3\OneDrive\Desktop\image-8.jpg")

# Sobel along X-axis
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# Sobel along Y-axis
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Convert to absolute values
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely)

# Combine X and Y edges
sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Sobel X", sobelx)
cv2.imshow("Sobel Y", sobely)
cv2.imshow("Sobel XY", sobelxy)

cv2.waitKey(0)
cv2.destroyAllWindows()
