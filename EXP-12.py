import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\tejv3\OneDrive\Desktop\image 11.jpg")

rows, cols, ch = img.shape

# Four points in the original image
pts1 = np.float32([[50, 50],
                   [300, 50],
                   [50, 300],
                   [300, 300]])

# Corresponding points in the output image
pts2 = np.float32([[0, 0],
                   [300, 0],
                   [300, 300],
                   [0, 300]])

# Compute perspective transformation matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

# Apply perspective transformation
dst = cv2.warpPerspective(img, M, (cols, rows))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Perspective Transformed Image", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
