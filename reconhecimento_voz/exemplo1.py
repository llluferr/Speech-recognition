from pocketsphinx import LiveSpeech

for frase in LiveSpeech():
    print("Voce falou: ", frase)