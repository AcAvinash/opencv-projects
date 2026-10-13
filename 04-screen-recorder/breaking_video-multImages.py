
import cv2
import os

# Set the folder path to save frames
save_path = r"D:\OpenCv\opencv-projects\04-screen-recorder\frames"

# Create the folder if it does not exist
os.makedirs(save_path, exist_ok=True)

# Open webcam
vidcap = cv2.VideoCapture(0)

if not vidcap.isOpened():
    print("Error: Camera could not be opened.")
    raise SystemExit

count = 0

while True:
    # Read a frame from the webcam
    ret, image = vidcap.read()

    if not ret:
        print("Could not read frame.")
        break

    # Create the full image path
    filename = os.path.join(save_path, f"imgN{count}.jpg")

    # Save the frame
    saved = cv2.imwrite(filename, image)

    if saved:
        print("Saved:", filename)
    else:
        print("Failed to save:", filename)

    # Display the webcam frame
    cv2.imshow("res", image)

    count += 1

    # Press q to stop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
vidcap.release()
cv2.destroyAllWindows()