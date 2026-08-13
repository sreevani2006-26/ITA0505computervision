import cv2

cap1 = cv2.VideoCapture(r"C:\Users\tejv3\Downloads\highway.mp4.mp4")
cap2 = cv2.VideoCapture(r"C:\Users\tejv3\Downloads\highway.mp4.mp4")

while True:
    ret1, frame1 = cap1.read()

    # Fast window advances every loop
    if ret1:
        cv2.imshow("Fast Video", frame1)

    # Slow window advances only every 3 loops
    if int(cap1.get(cv2.CAP_PROP_POS_FRAMES)) % 3 == 0:
        ret2, frame2 = cap2.read()
        if ret2:
            cv2.imshow("Slow Video", frame2)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
