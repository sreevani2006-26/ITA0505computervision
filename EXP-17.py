import cv2
import numpy as np
image = cv2.imread(r"C:\Users\tejv3\OneDrive\Desktop\image leena face")
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_x = np.absolute(sobel_x)
sobel_x = np.uint8(sobel_x)
cv2.imshow('Original Image', image)
cv2.imshow('Sobel X Edge Detection', sobel_x)
cv2.waitKey(0)
cv2.destroyAllWindows()
