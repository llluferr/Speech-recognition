import speech_recognition as sr

reconhecedor = sr.Recognizer()
microfone = sr.Microphone()

while True:
    try:
        with microfone as mic:
            reconhecedor.adjust_for_ambient_noise(mic)
            print("Fale algo...")
            audio = reconhecedor.listen(mic)
            print("Aguarde... reconhecendo audio...")
            print(reconhecedor.recognize_google(audio))
    except:
        print("Bugou algo...")