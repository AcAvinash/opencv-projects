
import cv2
import yt_dlp

url = "https://www.youtube.com/watch?v=S-z6vyR89Ig"

# Get YouTube stream URL
ydl_opts = {
    "format": "134",
    "noplaylist": True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)
    video_url = info["url"]

# Capture video
cap = cv2.VideoCapture(video_url)

if not cap.isOpened():
    print("Unable to open YouTube video")
    raise SystemExit

# Video properties
fps = cap.get(cv2.CAP_PROP_FPS)

if not fps or fps <= 0:
    fps = 25.0

width = 700
height = 500

# Define codec and output file
fourcc = cv2.VideoWriter_fourcc(*"XVID")

out = cv2.VideoWriter(
    r"D:\OpenCv\opencv-projects\03-opencv-mobile-camera-capture\youtube_video.avi",
    fourcc,
    fps,
    (width, height)
)

if not out.isOpened():
    print("Unable to create output video")
    cap.release()
    raise SystemExit

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Video stream ended")
        break

    frame = cv2.resize(frame, (width, height))

    cv2.imshow("YouTube Video", frame)

    # Save each frame
    out.write(frame)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Video saved successfully!")