
import cv2
import numpy as np

def mouse_event(event, x, y, flags, param):
    print(f"Mouse event: {event}, Position: ({x}, {y}), Flags: {flags}, Param: {param}")
    font = cv2.FONT_HERSHEY_PLAIN
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Left button clicked at: ({x}, {y})")
        cord = f". {x}, {y}"
        cv2.putText(img, cord, (x, y), font, 1, (155, 125, 100), 2)
        cv2.imshow('image', img)
    elif event == cv2.EVENT_RBUTTONDOWN:
        b = img[y, x, 0]  # Blue channel
        g = img[y, x, 1]  # Green channel
        r = img[y, x, 2]  # Red channel
        color_bgr = f". {b}, {g}, {r}"
        cv2.putText(img, color_bgr, (x, y), font, 1, (152, 255, 130), 2)
        cv2.imshow('image', img)

img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('image', img)

cv2.setMouseCallback('image', mouse_event)

cv2.waitKey(0)
cv2.destroyAllWindows()