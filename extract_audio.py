from moviepy.editor import VideoFileClip

def extract_audio(video_path):
    video = VideoFileClip(video_path)

    if video.audio is None:
        print("⚠️ No audio track found, skipping audio extraction.")
        return

    video.audio.write_audiofile("audio.wav", logger=None)
