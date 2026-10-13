import cv2
import datetime
cap = cv2.VideoCapture(r"D:\OpenCv\opencv-projects\06-shape-txt-on-Video\festival.mp4")
print( "Width of video frame:", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Height of video frame:", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Or you can use simpler way to get width and height of video frame
print("Width of video frame:", cap.get(3))
print("Height of video frame:", cap.get(4))

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, text, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, datet, (10, 100), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('Video Frame', frame)
        k = cv2.waitKey(250) 
        if k == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()