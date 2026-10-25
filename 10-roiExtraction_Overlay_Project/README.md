## 11. ROI Extraction & Object Overlay

### Description

This project demonstrates Region of Interest (ROI) extraction and basic object overlay using OpenCV and Python. The goal is to extract the Stormbreaker object from its source image and place it onto Thor's image by using thresholding, binary masks, and bitwise operations.

### Concepts Covered

- Image loading and resizing
- Grayscale conversion
- Binary thresholding and inverse thresholding
- Mask creation and background removal
- Region of Interest (ROI) extraction
- `cv2.bitwise_and()` for pixel selection
- `cv2.add()` for combining images
- Replacing an ROI in the destination image

### How It Works

1. Load and resize the Thor and Stormbreaker images.
2. Convert the Stormbreaker image to grayscale.
3. Apply binary and inverse thresholding to create complementary masks.
4. Extract an ROI from Thor's image.
5. Preserve Thor's pixels using the inverse mask.
6. Extract Stormbreaker's selected pixels using the binary mask.
7. Combine both images and place the result back into Thor's image.

### Technologies Used

- Python
- OpenCV



### Learning Outcome

Learned how to use thresholding, masks, bitwise operations, and ROI manipulation to perform basic foreground extraction and image compositing.

**Note:** The extraction quality depends on the threshold value and the contrast between the object and its background.
