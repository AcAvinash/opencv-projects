# OpenCV Mouse Events and Mouse Callback

## Description

This project demonstrates how to handle mouse events using OpenCV and Python. It includes drawing shapes with mouse clicks and finding pixel coordinates and BGR color values.

## Features

- Draw a circle using the left mouse button.
- Draw a rectangle using the right mouse button.
- Display pixel coordinates on the image.
- Find pixel color values in BGR format.
- Handle mouse events using `cv2.setMouseCallback()`.

## Technologies Used

- Python
- OpenCV (`cv2`)
- NumPy

## Concepts Learned

- Mouse Callback Function
- Mouse Events and Event Handling
- Drawing Shapes using OpenCV
- Pixel Coordinates `(x, y)`
- Accessing Pixel Values using `img[y, x]`
- BGR Color Channels
- Displaying Text using `cv2.putText()`

## How to Run

1. Install the required libraries:

   ```bash
   pip install opencv-python numpy
   ```
2. Run the Python script:

   ```bash
   python mouse_events.py
   ```
3. Use the mouse to draw shapes or explore pixel coordinates and color values.

## Controls

| Mouse / Key | Action                                |
| ----------- | ------------------------------------- |
| Left-click  | Draw a circle / display coordinates   |
| Right-click | Draw a rectangle / display BGR values |
| Esc         | Close the window (drawing project)    |

## Learning Outcome

Learned how to handle mouse events in OpenCV, draw shapes interactively, and access pixel coordinates and BGR color values.
