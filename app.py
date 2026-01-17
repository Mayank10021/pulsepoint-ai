import streamlit as st
from pipeline import process_video

st.set_page_config(page_title="PulsePoint AI", layout="centered")
st.title("PulsePoint AI")

video_file = st.file_uploader("Upload a long video", type=["mp4"])

if video_file:
    with open("input.mp4", "wb") as f:
        f.write(video_file.read())

    st.success("Video uploaded successfully!")

    if st.button("Generate Reels"):
        with st.spinner("Processing video..."):
            outputs = process_video("input.mp4")

        st.success("Reels generated!")

        for clip in outputs:
            st.video(clip)