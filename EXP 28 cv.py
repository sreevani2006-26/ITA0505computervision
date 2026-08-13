import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolo11n.pt")

# Your video path
video = cv2.VideoCapture(
    r"C:\Users\chint\Downloads\car-detection.mp4"
)

# Check whether video opened successfully
if not video.isOpened():
    print("Error: Could not open the video.")
    exit()

# Vehicle classes
vehicle_classes = {
    2: "Car",
    3: "Motorcycle",
    5: "Bus",
    7: "Truck"
}

while True:

    # Read a frame
    ret, frame = video.read()

    if not ret:
        print("Video completed.")
        break

    # Detect objects
    results = model(frame, verbose=False)

    # Process detected objects
    for result in results:

        for box in result.boxes:

            # Get class ID
            class_id = int(box.cls[0])

            # Get confidence
            confidence = float(box.conf[0])

            # Detect only vehicles
            if class_id in vehicle_classes:

                # Get coordinates
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Vehicle name
                vehicle_name = vehicle_classes[class_id]

                # Draw bounding box
                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                # Display vehicle name
                label = vehicle_name + " " + str(round(confidence * 100, 1)) + "%"

                cv2.putText(
                    frame,
                    label,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

    # Display frame
    cv2.imshow("Vehicle Detection", frame)

    # Press Q to stop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release video
video.release()
cv2.destroyAllWindows()

print("Vehicle detection completed.")
