
import cv2

img = cv2.imread(r"D:\OpenCv\opencv-projects\11-Simple_Thresholding\images\thresholding.jpeg")
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,img2 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)
_,img3 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY_INV)
_,img4 = cv2.threshold(img1,127,255,cv2.THRESH_TRUNC)
_,img5 = cv2.threshold(img1,127,255,cv2.THRESH_TOZERO)
_,img6 = cv2.threshold(img1,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow("original_img",img)
cv2.imshow("Grayscale",img1)
cv2.imshow("Binary_img",img2)
cv2.imshow("Inverse_img",img3)
cv2.imshow("Truncate",img4)
cv2.imshow("ToZero",img5)
cv2.imshow("ToZeroInv",img6)
cv2.waitKey(0)
cv2.destroyAllWindows()                 