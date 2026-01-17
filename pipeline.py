from extract_audio import extract_audio
from transcribe import transcribe_audio
from emotion_detector import select_timestamps
from clip_generator import generate_clips

def process_video(video_path):
    extract_audio(video_path)
    segments = transcribe_audio()
    timestamps = select_timestamps(segments)
    outputs = generate_clips(video_path, timestamps)
    return outputs