from gtts import gTTS

text = open("output/translated.txt", encoding="utf-8").read()

tts = gTTS(text=text, lang="ta")
tts.save("output/tts.wav")

print("Tamil TTS audio generated successfully (gTTS)")
