import cv2

img = cv2.imread(r"C:\Users\tejv3\OneDrive\Desktop\IMAGE 3.jpg")

# Bigger Size Scaling
bigger = cv2.resize(img, (1000, 700))

# Smaller Size Scaling
smaller = cv2.resize(img, (300, 200))

cv2.imshow("Original Image", img)

cv2.imshow("Bigger Image", bigger)

cv2.imshow("Smaller Image", smaller)

cv2.waitKey(0)

cv2.destroyAllWindows()
