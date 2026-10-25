import cv2
img1 = cv2.imread(r"D:\OpenCv\opencv-projects\10-roiExtraction_Overlay_Project\images\hero1.jpg")
img2 = cv2.imread(r"D:\OpenCv\opencv-projects\10-roiExtraction_Overlay_Project\images\strom_breaker.JPG")
img1 = cv2.resize(img1,(1024,650))
img2 = cv2.resize(img2,(600,650))
gray_img = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
_,mask = cv2.threshold(gray_img,50,255,cv2.THRESH_BINARY) #bg = dark ,storm breaker= white
_,mask1 = cv2.threshold(gray_img,50,255,cv2.THRESH_BINARY_INV) # bg= white ,storm breaker= black
r,c,ch = img2.shape
roi = img1[0:r,0:c]
img1_bg = cv2.bitwise_and(roi,roi,mask=mask1)

img2_bg = cv2.bitwise_and(img2,img2,mask=mask)

result = cv2.add(img1_bg,img2_bg)
img1[0:r,0:c]=result
cv2.imshow("result",result)
cv2.imshow("img1",img1)
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
# cv2.imshow("roi",roi)
# cv2.imshow("gray_img",gray_img)
# cv2.imshow("mask",mask)
# cv2.imshow("mask1",mask1)
cv2.waitKey(0)
cv2.destroyAllWindows()
