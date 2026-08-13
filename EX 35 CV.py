import cv2

# Function to add text to image
def add_text():
    # Load the given image
    image_path = r"C:\Users\chint\OneDrive\Pictures\person.jpg.jpg"
    image = cv2.imread(image_path)

    # Check if image is loaded
    if image is None:
        print("Error: Could not load the image.")
        return

    # Get text from user
    text = input("Enter the text to display on the image: ")

    # Add text to image
    cv2.putText(
        image,
        text,
        (50, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    # Display the image
    cv2.imshow("Image with Text", image)

    # Save the output image
    cv2.imwrite(
        r"C:\Users\chint\OneDrive\Pictures\text_image.jpg",
        image
    )

    print("Text added successfully.")

    # Wait and close
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Call the function
add_text()
