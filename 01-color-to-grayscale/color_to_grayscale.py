import cv2
import numpy as np

image = cv2.imread(r'D:\OpenCv\opencv-projects\01-color-to-grayscale\images\horse.jpg', 0)
cv2.imshow('Grayscale Image', image)
k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite(r"D:\OpenCv\opencv-projects\01-color-to-grayscale\images\horse_gray.jpg", image)
    print("Image saved as horse_gray.jpg")

cv2.destroyAllWindows()