# OpenCV Camera and Video Capture

This project demonstrates capturing and saving video using OpenCV.

## Features

* Capture video from a mobile IP camera.
* Read and display video frames.
* Save the camera feed as an AVI file.
* Read a YouTube video stream using `yt-dlp` and OpenCV.

## Requirements

```bash
pip install opencv-python yt-dlp
```

For mobile camera capture, use an IP camera app and replace the sample URL with your camera's video stream URL.

For YouTube capture, run the script with a valid YouTube URL and an available format ID.

## Run

```bash
python filename.py
```

Press **q** to stop capturing and close the video window.

**Note:** YouTube stream formats may change, and the selected format may contain video only, without audio.
