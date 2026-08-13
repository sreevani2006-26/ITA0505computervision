import cv2

# Load the image
image_path = r"C:\Users\chint\OneDrive\Pictures\person.jpg.jpg"
image = cv2.imread(image_path)

# Check whether image is loaded correctly
if image is None:
    print("Error: Could not load the image.")
    print("Check the image path.")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load Haar Cascade for eye detection
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

# Detect eyes
eyes = eye_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(20, 20)
)

# Draw rectangles around detected eyes
for (x, y, w, h) in eyes:
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

# Display number of detected eyes
print("Number of eyes detected:", len(eyes))

# Display the result
cv2.imshow("Eye Detection", image)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
