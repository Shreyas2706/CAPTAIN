import pywhatkit as kit
import pyautogui as pt
import os
import pyaudio 
import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import smtplib
global xyz
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
         speak("Good Evening!")

    speak("hello SHREYAS!!  how are you ")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def takeMessage():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
try:
    def work():

        query = takeCommand().lower()

        if "captain" in query:
            query = query.replace("captain" , "").strip()
            print(query)
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            if "home" in query:
                pt.hotkey("win", "d")

            if "just" in query:
                query = query.replace("just" , "")
                pt.write(query)

            # if "screenshot" in query:
            #     pyautogui.scroll(100 , 100)
            if 'out' in query:
                print('Exiting Code')
                return 'exit'
            
            if 'open' in query:
                name = query.replace("open" , "").strip()
                webbrowser.open(f"{name}.com")

            if 'play' in query:
                song = query.replace("play", "")
                # search_url = f"https://www.youtube.com/results?search_query={song.replace(' ', '+')}"
                # webbrowser.open(search_url)
                pt.press("home")
                kit.playonyt(song)

                if 'volume up' in query:
                    speak("By how much percent do you want to increase the volume?")
                    volume_change = int(takeCommand())
                    current_volume = pt.volumeInfo().get('volume')
                    new_volume = min(current_volume + volume_change, 100)  # Ensure volume doesn't exceed 100
                    pt.press("volumeup", new_volume)
                    speak(f"Volume increased by {volume_change} percent.")

                elif 'volume down' in query:
                    speak("By how much percent do you want to decrease the volume?")
                    volume_change = int(takeCommand())
                    current_volume = pt.volumeInfo().get('volume')
                    new_volume = max(current_volume - volume_change, 0)  # Ensure volume doesn't go below 0
                    pt.press("volumedown", new_volume)
                    speak(f"Volume decreased by {volume_change} percent.")

            if ('pause' in query ) or ("stop" in query):
                pt.press("k")
                
            if ('play' in query ) or ("resume" in query):
                pt.press("k")

            if 'the time' in query:
                 whatsappstrTime = datetime.datetime.now().stkrftime(" ")
                 speak("{}, the time is {}".format('SHREYAS ', strTime))

            if 'shutdown' in query:
                try:
                    speak("say continue to shutdown ?")
                    content = takeCommand().lower()
                    if content == 'continue':
                        speak("proceeding to shutdown in 3!!! 2!!! 1!!!")
                        os.system('shutdown /s /t 2')
                    else:
                        speak('okay!!')
                except Exception as e:
                    print(e)
                    speak("Sorry SHREYAS. I am not able to shutdown right now")
              
              
            if 'reboot' in query:
                try:
                    speak("say continue to reboot ?")
                    content = takeCommand().lower()
                    if content == 'continue':
                        speak("proceeding to reboot in 3!!! 2!!! 1!!!")
                        os.system('shutdown /r /t 2')
                    else:
                        speak('okay!!')
                except Exception as e:
                    print(e)
                    speak("Sorry SHREYAS. I am not able to reboot right now")
                  

            if 'open code' in query:
                codePath = 'path of the code'
                os.startfile(codePath)

            if 'email to SHREYAS' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "SHREYASmail@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry SHREYAS. I am not able to send this email")
            else:
                print("No query matched")
except Exception as e:
    print(e)
    speak("Sorry SHREYAS. please say it again")
    

if __name__ == "__main__":
    speak("!! Initializing Captain")
    wishMe()
    while True:
        a=work()
        if a == 'exit':
            speak('!!!!Exiting code')
            break
 