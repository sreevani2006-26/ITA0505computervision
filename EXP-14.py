import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\tejv3\OneDrive\Desktop\image 11.jpg")

h, w = img.shape[:2]

# Four points in original image
pts1 = np.float32([
    [100, 100],
    [400, 100],
    [100, 300],
    [400, 300]
])

# Corresponding points in transformed image
pts2 = np.float32([
    [50, 50],
    [450, 80],
    [100, 350],
    [420, 320]
])

# Compute Homography Matrix
H, status = cv2.findHomography(pts1, pts2)

# Apply Homography Transformation
result = cv2.warpPerspective(img, H, (w, h))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Homography Transformed Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
