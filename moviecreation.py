from moviepy.editor import VideoFileClip, concatenate_videoclips

# List of MKV files in sequential order
videos = ["C:/Users/joeyh/Videos/final.mkv"]

# Load videos
clips = [VideoFileClip(video) for video in videos]

# Concatenate the clips
final_clip = concatenate_videoclips(clips, method="compose")

# Export as MP4 (since MKV is not a common output format)
final_clip.write_videofile("C:/Users/joeyh/Videos/final.mp4", codec="libx264", fps=30)
