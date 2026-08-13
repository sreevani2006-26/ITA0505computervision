import cv2

# Function to play video in reverse slow motion
def reverse_slow_motion():

    # Video path
    video_path = r"C:\Users\chint\OneDrive\Pictures\WhatsApp Video 2026-07-28 at 11.11.20 AM.mp4"

    # Open the video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open the video.")
        return

    # Store all frames
    frames = []

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    print("Total frames:", len(frames))

    # Play video in reverse slow motion
    for frame in reversed(frames):

        cv2.imshow("Reverse Slow Motion", frame)

        # 100 ms delay for slow motion
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


# Call the function
reverse_slow_motion()
