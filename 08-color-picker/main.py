import numpy as np
import cv2

def cross(x):
    pass
#white image
img = np.ones((512, 512, 3), np.uint8) * 255
cv2.namedWindow("color picker")

# creating switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'color picker', 0, 1, cross)

# creating trackbars for adjusting colors
cv2.createTrackbar('R', 'color picker', 0, 255, cross)
cv2.createTrackbar('G', 'color picker', 0, 255, cross)
cv2.createTrackbar('B', 'color picker', 0, 255, cross)

# creating logic to handle trackbars
while True:
    cv2.imshow("color picker", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # for exit
        break

    # set current positions of four bars
    s = cv2.getTrackbarPos(switch, "color picker")  # switch
    r = cv2.getTrackbarPos('R', 'color picker')
    g = cv2.getTrackbarPos('G', 'color picker')
    b = cv2.getTrackbarPos('B', 'color picker')

    if s == 0:
        img[:] = 255  # white background
    else:
        img[:] = [b, g, r]  # here OpenCV supports BGR

cv2.destroyAllWindows()