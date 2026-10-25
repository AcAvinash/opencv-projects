import cv2

img = cv2.imread(r"D:\OpenCv\opencv-projects\12-Adaptive_Threshold\images\thresholding.jpeg")

if img is None:
    print("Image load nahi hui, path check karo!")
else:
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, img2 = cv2.threshold(
        img1, 127, 255, cv2.THRESH_BINARY
    )

    # Adaptive Mean
    img3 = cv2.adaptiveThreshold(
        img1, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY, 11, 2
    )

    # Adaptive Gaussian
    img4 = cv2.adaptiveThreshold(
        img1, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2
    )

    print("Gaussian output:", img4.shape)

    cv2.imshow("Original Image", img)
    cv2.imshow("Grayscale", img1)
    cv2.imshow("Simple Threshold", img2)
    cv2.imshow("Adaptive Mean", img3)
    cv2.imshow("Adaptive Gaussian", img4)

    cv2.waitKey(0)
    cv2.destroyAllWindows()