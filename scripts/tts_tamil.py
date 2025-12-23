from indic_tts import TTS

text = open("output/translated.txt", encoding="utf-8").read()

tts = TTS(language="ta")
tts.save(text, "output/tts.wav")

print("Tamil TTS audio generated successfully")
