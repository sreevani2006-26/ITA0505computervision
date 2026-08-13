import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread(r"C:\Users\tejv3\OneDrive\Desktop\8.jpg")

# Check if image loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Scharr gradients
grad_x = cv2.Scharr(blurred, cv2.CV_64F, 1, 0)
grad_y = cv2.Scharr(blurred, cv2.CV_64F, 0, 1)

# Gradient magnitude
gradient_magnitude = np.sqrt(grad_x**2 + grad_y**2)

# Normalize
gradient_magnitude = cv2.normalize(
    gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX
)

gradient_magnitude = np.uint8(gradient_magnitude)

# Sharpen image
sharpened = cv2.addWeighted(gray, 1.5, gradient_magnitude, -0.5, 0)

# Save output
cv2.imwrite(r"C:\Users\tejv3\OneDrive\Desktop\sharpened.jpg", sharpened)

# Display using Matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(gray, cmap='gray')
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(sharpened, cmap='gray')
plt.title("Sharpened Image")
plt.axis("off")

plt.show()
