import cv2
import numpy as np

# Function to create image and draw circle
def create_circle():
    # Get image size from user
    height = int(input("Enter image height: "))
    width = int(input("Enter image width: "))

    # Create a white image
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Find the center of the image
    center_x = width // 2
    center_y = height // 2

    # Set circle radius
    radius = min(width, height) // 4

    # Draw circle
    cv2.circle(
        image,
        (center_x, center_y),
        radius,
        (0, 0, 255),
        3
    )

    # Display image
    cv2.imshow("Circle", image)

    # Save image
    cv2.imwrite("circle.jpg", image)

    # Wait and close
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Call the function
create_circle()
