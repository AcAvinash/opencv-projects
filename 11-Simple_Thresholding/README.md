
## 11. Simple Thresholding

### Description

This project demonstrates different types of image thresholding techniques using OpenCV and Python. The input image is converted to grayscale, and five thresholding methods are applied to understand how pixel intensities are modified.

### Concepts Covered

- Loading and displaying images
- BGR to grayscale conversion
- Simple thresholding using `cv2.threshold()`
- Binary Thresholding (`THRESH_BINARY`)
- Inverse Binary Thresholding (`THRESH_BINARY_INV`)
- Truncated Thresholding (`THRESH_TRUNC`)
- To Zero Thresholding (`THRESH_TOZERO`)
- Inverse To Zero Thresholding (`THRESH_TOZERO_INV`)

### Thresholding Methods

1. **Binary:** Pixel values above 127 become 255; the remaining pixels become 0.
2. **Binary Inverse:** Pixel values above 127 become 0; the remaining pixels become 255.
3. **Truncate:** Pixel values above 127 are set to 127; other values remain unchanged.
4. **To Zero:** Pixel values at or below 127 become 0; higher values remain unchanged.
5. **To Zero Inverse:** Pixel values above 127 become 0; lower or equal values remain unchanged.

### Technologies Used

- Python
- OpenCV

### Learning Outcome

Learned how different thresholding techniques transform grayscale images based on a threshold value and a maximum pixel value.

### Threshold Parameters

- **Threshold value:** 127
- **Maximum value:** 255
- **Input image:** `thresholding.jpeg`
