import cv2
import numpy as np

# Function for background subtraction based on color
def subtract_background():

    # Load the image
    image_path = r"C:\Users\chint\OneDrive\Pictures\person.jpg.jpg"
    image = cv2.imread(image_path)

    # Check if image is loaded
    if image is None:
        print("Error: Could not load the image.")
        return

    # Convert image from BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define color levels for background
    # Example: remove green background
    lower = np.array([35, 40, 40])
    upper = np.array([85, 255, 255])

    # Create mask for the background color
    mask = cv2.inRange(hsv, lower, upper)

    # Subtract the background
    result = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask))

    # Display original image
    cv2.imshow("Original Image", image)

    # Display background mask
    cv2.imshow("Background Mask", mask)

    # Display result
    cv2.imshow("Background Removed", result)

    # Save result
    cv2.imwrite(
        r"C:\Users\chint\OneDrive\Pictures\background_removed.jpg",
        result
    )

    print("Background subtraction completed.")

    # Wait and close
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Call the function
subtract_background()
