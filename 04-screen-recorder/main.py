import cv2 as c
import pyautogui as p
import numpy as np

screen_size = p.size()
width, height = screen_size.width, screen_size.height


fn = input(
    "Enter the full path to save recording (.avi): "
).strip().strip('"')

fourcc = c.VideoWriter_fourcc(*"XVID")

output = c.VideoWriter(
    fn,
    fourcc,
    20.0,
    (width, height)
)

if not output.isOpened():
    print("Error: VideoWriter could not open the file.")
    print("Check the file path, extension, and codec.")
    raise SystemExit

c.namedWindow("Recording", c.WINDOW_NORMAL)
c.resizeWindow("Recording", 480, 270)

print("Screen recording started. Press 'q' to stop.")

try:
    while True:
        # Capture screenshot
        img = p.screenshot()

        # Convert RGB image to BGR for OpenCV
        frame = c.cvtColor(
            np.array(img),
            c.COLOR_RGB2BGR
        )

        output.write(frame)

        c.imshow("Recording", frame)

        if c.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    output.release()
    c.destroyAllWindows()

print("Recording saved to:", fn)