import cv2
import numpy as np

# Function to extract foreground based on color
def subtract_foreground():

    # Load the image
    image_path = r"C:\Users\chint\OneDrive\Pictures\person.jpg.jpg"
    image = cv2.imread(image_path)

    # Check if image is loaded
    if image is None:
        print("Error: Could not load the image.")
        return

    # Convert image to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define color levels for the foreground
    # Example: detecting green foreground
    lower = np.array([35, 40, 40])
    upper = np.array([85, 255, 255])

    # Create mask for foreground
    mask = cv2.inRange(hsv, lower, upper)

    # Extract foreground
    foreground = cv2.bitwise_and(image, image, mask=mask)

    # Display original image
    cv2.imshow("Original Image", image)

    # Display foreground mask
    cv2.imshow("Foreground Mask", mask)

    # Display extracted foreground
    cv2.imshow("Foreground", foreground)

    # Save foreground
    cv2.imwrite(
        r"C:\Users\chint\OneDrive\Pictures\foreground.jpg",
        foreground
    )

    print("Foreground subtraction completed.")

    # Wait and close
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Call the function
subtract_foreground()
