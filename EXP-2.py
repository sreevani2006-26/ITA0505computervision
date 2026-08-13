import cv2

img = cv2.imread(r"C:\Users\tejv3\OneDrive\Desktop\image-1.jpg")

img = cv2.resize(img, (600, 400))

blur = cv2.GaussianBlur(img, (15, 15), 0)

cv2.imshow("Original Image", img)

cv2.imshow("Blur Image", blur)

cv2.waitKey(0)

cv2.destroyAllWindows()
