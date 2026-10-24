import cv2
import numpy as np

img = cv2.imread(r"D:\OpenCv\opencv-projects\09-roi\roi_opr.jpg")
print(img.shape)
img = cv2.resize(img,(800,800))

#y:=53 x:315 x1:451 y1;210
roi = img[53:210,315:451]
# difference 210-53=157, 451-315=136
# now passing image to data
img[53:210,452:588] = roi

img1 = cv2.imread(r"D:\OpenCv\opencv-projects\09-roi\ironman.jpg")
img1 = cv2.resize(img1,(900,600))
img1[4:161,550:686]=roi
cv2.imshow("img",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()