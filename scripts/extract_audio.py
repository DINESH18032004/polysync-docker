import subprocess

subprocess.run([
    "ffmpeg", "-y",
    "-i", "input/input.mp4",
    "-ar", "16000",
    "-ac", "1",
    "output/audio.wav"
], check=True)

print("Audio extracted successfully")
