
## 12. Adaptive Thresholding

### Description

This project demonstrates Adaptive Thresholding techniques using OpenCV and Python. It compares Simple Thresholding, Adaptive Mean Thresholding, and Adaptive Gaussian Thresholding to understand how different methods convert grayscale images into binary images.

### Concepts Covered

- Image loading and validation
- BGR to grayscale conversion
- Simple Thresholding using `cv2.threshold()`
- Adaptive Mean Thresholding
- Adaptive Gaussian Thresholding
- Understanding local threshold values
- Displaying multiple image outputs using `cv2.imshow()`

### Thresholding Methods

1. **Simple Thresholding:** Uses a fixed threshold value of 127 for the entire image.
2. **Adaptive Mean Thresholding:** Calculates the local threshold using the mean of neighboring pixel intensities.
3. **Adaptive Gaussian Thresholding:** Calculates the local threshold using a weighted sum of neighboring pixel intensities, where closer pixels receive more weight.

### Parameters Used

- **Maximum pixel value:** 255
- **Adaptive method:** Mean and Gaussian
- **Threshold type:** `cv2.THRESH_BINARY`
- **Block size:** 11
- **Constant C:** 2

### Technologies Used

- Python
- OpenCV

### Learning Outcome

Learned how adaptive thresholding calculates local thresholds and how it differs from simple thresholding, especially when an image has uneven lighting or varying brightness.

### Error Handling

Used an `if img is None` condition to check whether the image was loaded successfully before processing it.
