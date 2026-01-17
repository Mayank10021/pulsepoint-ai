from moviepy.editor import VideoFileClip
import os


def generate_clips(video_path, timestamps):
    os.makedirs("output_clips", exist_ok=True)

    video = VideoFileClip(video_path)
    duration = video.duration

    output_files = []

    for i, (start, end) in enumerate(timestamps):
        start = max(0, start)
        end = min(end, duration)

        if start >= end or start >= duration:
            continue

        clip = video.subclip(start, end)
        out = f"output_clips/reel_{i+1}.mp4"

        clip.write_videofile(
            out,
            codec="libx264",
            audio_codec="aac",
            logger=None
        )

        output_files.append(out)

    video.close()
    return output_files
