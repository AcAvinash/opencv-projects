import cv2

cap = cv2.VideoCapture(r"D:\OpenCv\opencv-projects\02-opencv-video-frame-viewer\festival.mp4")
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (700, 500))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Video Frame', frame)
    cv2.imshow('Gray Video Frame', gray)
    k = cv2.waitKey(250) 
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()