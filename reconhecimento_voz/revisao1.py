from gtts import gTTS
from playsound import playsound



msg = ""

audio = gTTS(msg, lang='pt', slow=True)
audio.save('fazol.mp3')
playsound('fazol.mp3')