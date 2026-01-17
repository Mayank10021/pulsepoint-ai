from extract_audio import extract_audio
from transcribe import transcribe_audio
from emotion_detector import select_timestamps
from clip_generator import generate_clips
from moviepy.editor import VideoFileClip


def process_video(video_path):
    extract_audio(video_path)

    segments = transcribe_audio()

    timestamps = select_timestamps(segments)

    video = VideoFileClip(video_path)
    duration = video.duration

    safe_timestamps = []

    if timestamps:
        for start, end in timestamps:
            start = max(0, start)
            end = min(end, duration)

            if start < end:
                safe_timestamps.append((start, end))

    if not safe_timestamps:
        clip_len = min(15, duration)
        safe_timestamps = [(0, clip_len)]

    outputs = generate_clips(video_path, safe_timestamps)
    return outputs
