import cv2

# Function to count faces
def count_faces():

    # Load the image
    image_path = r"C:\Users\chint\OneDrive\Pictures\person.jpg.jpg"
    image = cv2.imread(image_path)

    # Check if image is loaded
    if image is None:
        print("Error: Could not load the image.")
        return

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load Haar Cascade for face detection
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    # Count faces
    face_count = len(faces)

    print("Number of faces detected:", face_count)

    # Display the image
    cv2.imshow("Face Detection", image)

    # Wait and close
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Call the function
count_faces()
