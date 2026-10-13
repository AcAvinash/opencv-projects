# 04 - Screen Recorder

A Python project using OpenCV to record the computer screen and capture webcam frames.

## Features

- Screen recording saved as an AVI video.
- Webcam frame capture saved as JPG images.
- Live preview of screen recording and webcam.
- Press `q` to stop recording.

## Technologies Used

- Python
- OpenCV
- PyAutoGUI
- NumPy

## Project Structure

```text
04-screen-recorder/
├── main.py
├── frames/
│   ├── imgN0.jpg
│   └── ...
└── README.md
```

## How to Run

```bash
pip install opencv-python pyautogui numpy
python main.py
```

Enter the output video path when prompted to save the screen recording.
