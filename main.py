from gtts import gTTS
import os

text = "Hi! My name is Durbek Kholdarov! Student of FB TUIT"

language = 'en'
tts = gTTS(text=text, lang=language, slow=False)

audio_file = "output.mp3"
tts.save(audio_file)