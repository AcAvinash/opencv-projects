import cv2
import numpy as np

# img = cv2.imread(r"D:\OpenCv\opencv-projects\05-drawing line\thor.jpg")
# img = cv2.resize(img, (600, 700))

# Blank image of background color black
# img = np.zeros((512, 512, 3), np.uint8)

# Blank image of background color white
img = np.ones((512, 512, 3), np.uint8) * 255

img = cv2.line(img, (0, 0), (200, 200), (154, 92, 424), 8)

# arrowed line accept also accpet 5 parameter  (img,starting,ending,color,thickness)
img = cv2.arrowedLine(img, (0, 125), (255, 255), (255, 0, 125), 10)

# rectangle - accept parameter(img,start_co,end_co,colot ,thickness)
img = cv2.rectangle(img, (384, 10), (510, 128), (128, 0, 255), 8)
# -ve to fill the rectangle with color
img = cv2.rectangle(img, (384, 10), (510, 128), (128, 0, 255), -1)

# circle - accept(img,star_co,radius,color,thickness)
img = cv2.circle(img, (447, 125), 63, (214, 255, 0), -1)

# if i pass positive value in thickness then it will draw the circle with that thickness and if i pass negative value in thickness then it will fill the circle with color
img = cv2.circle(img, (447, 125), 63, (214, 255, 0), 5)

# font = cv2.FONT_ITALIC
# puttext -accept(img,text,start_co,font,fontsize,color,thickness,linetype
img = cv2.putText(img, 'THOR', (20, 500), cv2.FONT_ITALIC, 4, (0, 125, 255), 10, cv2.LINE_AA)

# ellipse-accept(img,start_cor,(length,height),color,thickness)
img = cv2.ellipse(img, (400, 600), (100, 50), 0, 0, 180, 155, 5)



cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()