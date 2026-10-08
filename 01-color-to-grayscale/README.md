
# Color to Grayscale Image Conversion using OpenCV

This project demonstrates how to read a color image as a grayscale image using OpenCV.

## What I Learned

* How to read an image using `cv2.imread()`
* How to read an image directly in grayscale mode using `flag = 0`
* How a grayscale image uses a single channel
* How to display an image using `cv2.imshow()`
* How to wait for a keyboard event using `cv2.waitKey()`
* How to save an image using `cv2.imwrite()`
* How to close OpenCV windows using `cv2.destroyAllWindows()`

## Code

```python
import cv2

image = cv2.imread("images/horse.jpg", 0)

cv2.imshow("Grayscale Image", image)

k = cv2.waitKey(0)

if k == ord('s'):
    cv2.imwrite("images/horse_gray.jpg", image)
    print("Image saved as horse_gray.jpg")

cv2.destroyAllWindows()
```

## How It Works

```text
Color Image
     ↓
cv2.imread(..., 0)
     ↓
Grayscale Image
     ↓
cv2.imshow()
     ↓
Press a key
     ↓
Press 's' → Save grayscale image
     ↓
cv2.destroyAllWindows()
```

## Important Note

In this project, `0` is used to load the image directly as grayscale, so `cv2.cvtColor()` is not required.
