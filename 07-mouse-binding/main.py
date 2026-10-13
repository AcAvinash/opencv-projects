import cv2
import numpy as np

def draw(event, x, y, flags, param):
    print(f"Mouse event: {event}, Position: ({x}, {y}), Flags: {flags}, Param: {param}")
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Left button clicked at: ({x}, {y})")
        cv2.circle(img, (x, y), 100, (125, 0, 255), 5)
    elif event == cv2.EVENT_RBUTTONDOWN:
        print(f"Right button clicked at: ({x}, {y})")
        cv2.rectangle(img, (x - 100, y - 100), (x + 100, y + 75), (125,125,255), 2)

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:  #esc
        break

cv2.destroyAllWindows()


