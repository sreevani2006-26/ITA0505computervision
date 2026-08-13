import cv2

# Read image
image = cv2.imread(r"C:\Users\tejv3\OneDrive\Desktop\IMAGE-4.jpg")

# Resize original image
image = cv2.resize(image, (600, 400))

# Rotate image
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Display images
cv2.imshow("Original Image", image)

cv2.imshow("Rotated Image", rotated)

# Wait for key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
