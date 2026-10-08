import cv2

cap = cv2.VideoCapture(0)

#Save the video to a file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(r'D:\OpenCv\opencv-projects\02-opencv-video-frame-viewer\output.avi', fourcc, 20.0, (700, 500))

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
      frame = cv2.resize(frame, (700, 500))
      output.write(frame)
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      cv2.imshow('Video Frame', frame)
      cv2.imshow('Gray Video Frame', gray)
      k = cv2.waitKey(250) 
      if k == ord('q'):
          break

cap.release()
output.release()
cv2.destroyAllWindows()