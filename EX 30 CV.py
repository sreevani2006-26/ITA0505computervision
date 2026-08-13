import cv2

# Load the image
image_path = r"C:\Users\chint\OneDrive\Pictures\person.jpg.jpg"
image = cv2.imread(image_path)

# Check if image is loaded
if image is None:
    print("Error: Could not load the image.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load Haar Cascade classifiers
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(100, 100)
)

# Detect smiles within each face
for (x, y, w, h) in faces:
    # Draw rectangle around face
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]

    smiles = smile_cascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.7,
        minNeighbors=20,
        minSize=(25, 25)
    )

    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(
            roi_color,
            (sx, sy),
            (sx + sw, sy + sh),
            (0, 255, 0),
            2
        )

print("Faces detected:", len(faces))

# Show the result
cv2.imshow("Smile Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
