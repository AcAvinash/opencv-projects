import cv2

camera = "http://192.168.1.100:8080/video"  # Replace with your IP camera URL
cap = cv2.VideoCapture(camera)
cap.open(camera)
print("Checking if camera is opened:", cap.isOpened())

fourcc = cv2.VideoWriter_fourcc(*'XVID')
# 0 for grayscale, default is 1 for color. If you want to save in grayscale, uncomment the line below and comment the next one.
#output = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480),0)

output = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Resize the frame to 640x480
    frame = cv2.resize(frame, (640, 480))

    # Display the resulting frame
    cv2.imshow('Camera Feed', frame)

    # Write the frame to the output file
    output.write(frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the camera and output file, and close all OpenCV windows
cap.release()
output.release()
cv2.destroyAllWindows()
