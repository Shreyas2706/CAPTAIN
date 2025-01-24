import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os
import smtplib
import pywhatkit as kit
import pyautogui as pt

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello, How can I assist you?")


def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"You said: {command}")
    except Exception as e:
        print(e)
        speak("Sorry, I didn't catch that. Can you please repeat?")
        return "None"

    return command.lower()


def execute_command(command):
    if 'wikipedia' in command:
        speak('Searching Wikipedia...')
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=2)
        speak("According to Wikipedia")
        speak(results)
    elif 'open' in command:
        website = command.split('open ')[-1]
        webbrowser.open(f"https://www.{website}.com")
    elif 'play' in command:
        song = command.replace("play", "")
        kit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time}")
    elif 'shutdown' in command:
        speak("Shutting down the system")
        os.system("shutdown /s /t 1")
    elif 'restart' in command:
        speak("Restarting the system")
        os.system("shutdown /r /t 1")
    elif 'email' in command:
        speak("Sorry, I can't send emails right now.")
    elif 'exit' in command:
        speak("Exiting the program")
        return False
    else:
        speak("Sorry, I couldn't understand that.")

    return True


if __name__ == "__main__":
    wish_me()
    while True:
        command = listen_command()
        if 'exit' in command:
            break
        execute_command(command)
