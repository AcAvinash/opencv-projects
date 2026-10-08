# OpenCV Video Frame Viewer

This project demonstrates how to read, process, display, and save videos using OpenCV.

## 1. Video Frame Viewer

The first program reads a video file using `cv2.VideoCapture()` and processes it frame by frame.

### Features:

- Reads an MP4 video file.
- Resizes each frame to `700 x 500`.
- Converts the frame from BGR to grayscale.
- Displays both the original and grayscale video.
- Uses `cv2.waitKey()` to control the video playback.
- Press `q` to stop the video.
- Releases the video resource after processing.

### Input:

`festival.mp4`

---

## 2. Webcam Video Recorder

The second program captures live video from the default webcam using `cv2.VideoCapture(0)`.

### Features:

- Captures live video from the webcam.
- Resizes each frame to `700 x 500`.
- Converts frames to grayscale.
- Displays the original and grayscale video.
- Saves the original BGR frames into an AVI video file.
- Uses XVID codec with `20 FPS`.
- Press `q` to stop recording.
- Releases the camera and output video resources.

### Output:

`output.avi`

### VideoWriter Configuration:

```python
fourcc = cv2.VideoWriter_fourcc(*'XVID')

output = cv2.VideoWriter(
    'output.avi',
    fourcc,
    20.0,
    (700, 500)
)
```

# How to Stop

Press:

<pre class="overflow-visible! px-0!" data-start="1658" data-end="1671"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>q</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

to stop video playback or webcam recording.
