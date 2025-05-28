# Task 2: Speech-to-Text System
# Objective: Transcribe audio using the SpeechRecognition library

import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Load audio file
audio_file = "Task2/harvard.wav"

# Transcribe audio
with sr.AudioFile(audio_file) as source:
    audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        print("Transcription:", text)
        # Save transcription to a file
        with open("Task2/transcription.txt", "w") as f:
            f.write(text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Error: {e}")

#Real-time microphone input
"""
with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source, timeout=5)
    try:
        text = recognizer.recognize_google(audio)
        print("Transcription:", text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Error: {e}")
"""