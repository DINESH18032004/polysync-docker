import whisper

model = whisper.load_model("base")
result = model.transcribe("output/audio.wav")

with open("output/transcript.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("Transcription completed successfully")
