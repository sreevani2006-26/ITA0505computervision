import cv2

# Read images
img = cv2.imread(r"C:\Users\tejv3\OneDrive\Desktop\WATEERMARK.jpg")
logo = cv2.imread(r"C:\Users\tejv3\OneDrive\Desktop\WATERMARK.jpg")

# Check if images loaded successfully
if img is None:
    print("Error: Main image not found!")
    exit()

if logo is None:
    print("Error: Logo image not found!")
    exit()

# Resize logo (adjust size as needed)
logo = cv2.resize(logo, (150, 150))

# Get dimensions
h_img, w_img, _ = img.shape
h_logo, w_logo, _ = logo.shape

# Calculate center position
center_x = w_img // 2
center_y = h_img // 2

left_x = center_x - w_logo // 2
top_y = center_y - h_logo // 2

right_x = left_x + w_logo
bottom_y = top_y + h_logo

# Extract ROI
roi = img[top_y:bottom_y, left_x:right_x]

# Blend logo with ROI
result = cv2.addWeighted(roi, 1.0, logo, 0.5, 0)

# Replace ROI in original image
img[top_y:bottom_y, left_x:right_x] = result

# Save output
cv2.imwrite(r"C:\Users\tejv3\OneDrive\Desktop\watermarked.jpg", img)

# Display result
cv2.imshow("Watermarked Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
