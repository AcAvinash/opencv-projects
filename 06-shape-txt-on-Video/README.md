# 06 - Display Text on Video

This project demonstrates how to display video properties, current date, and time on video frames using OpenCV and Python.

## Features

- Reads a video file using OpenCV.
- Displays video frame width and height.
- Shows the current date and time on each frame.
- Uses text overlays with custom font, color, and thickness.
- Press `q` to stop video playback.

## Technologies Used

- Python
- OpenCV
- datetime

## Concepts Learned

- `cv2.CAP_PROP_FRAME_WIDTH`
- `cv2.CAP_PROP_FRAME_HEIGHT`
- `cap.get()`
- `cv2.putText()`
- `datetime.datetime.now()`
- `cv2.waitKey()`
- `cap.release()`

## How to Run

Install OpenCV:

```bash
pip install opencv-python
```

Run the script:

```bash
python main.py
```

Make sure `festival.mp4` is available at the path specified in the Python script.

## Learning Outcome

Learned how to retrieve video properties and overlay dynamic text, including the current date and time, on video frames using OpenCV.
