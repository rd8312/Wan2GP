# pip install gTTS
from gtts import gTTS
with open("script.txt", "r", encoding="utf-8") as f:
    text = f.read()
tts = gTTS(text, lang="en", slow=False)
tts.save("30sec_color_lesson.mp3")
print("Done!  File saved as 30sec_color_lesson.mp3")
