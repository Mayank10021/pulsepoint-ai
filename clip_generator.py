from moviepy.editor import VideoFileClip
import os

def generate_clips(video_path, timestamps):
    os.makedirs("output_clips", exist_ok=True)
    video = VideoFileClip(video_path)

    output_files = []
    for i, (start, end) in enumerate(timestamps):
        clip = video.subclip(start, end)
        out = f"output_clips/reel_{i+1}.mp4"
        clip.write_videofile(out, logger=None)
        output_files.append(out)

    return output_files