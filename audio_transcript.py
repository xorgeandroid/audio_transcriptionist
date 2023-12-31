import speech_recognition as sr

# File path
audio_file = "audiofile Path.wav"

# Class `AudioSegment` by pydub
audio = sr.AudioFile(audio_file)

# Start Recognizer
recognizer = sr.Recognizer()

# Transcript
with audio as source:

    audio_data = recognizer.record(source)

    # using Google's speech recognition service
    text = recognizer.recognize_google(audio_data, language="es-ES")


    print("Text transcript:")
    print(text)