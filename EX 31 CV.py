import cv2

# Load the image
image_path = r"C:\Users\chint\OneDrive\Pictures\person.jpg.jpg"
image = cv2.imread(image_path)

# Check if image is loaded
if image is None:
    print("Error: Could not load the image.")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Set threshold value
threshold_value = 127

# Apply threshold segmentation
_, segmented = cv2.threshold(
    gray,
    threshold_value,
    255,
    cv2.THRESH_BINARY
)

# Display original image
cv2.imshow("Original Image", image)

# Display grayscale image
cv2.imshow("Grayscale Image", gray)

# Display segmented image
cv2.imshow("Segmented Image", segmented)

# Save the segmented image
cv2.imwrite(
    r"C:\Users\chint\OneDrive\Pictures\segmented_image.jpg",
    segmented
)

print("Segmentation completed successfully.")
print("Threshold value:", threshold_value)

# Wait for key press
cv2.waitKey(0)

# Close windows
cv2.destroyAllWindows()
