import speech_recognition as sr
import pyaudio
import setuptools
import pyttsx3
import webbrowser as wb
import musiclibrary
import os
import google 
# from google import genai
import google.generativeai as genai

recognizer=sr.Recognizer()
engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 


def speak_old(text):
    engine.say(text)
    engine.runAndWait()


# Directly configure Gemini API key
genai.configure(api_key="<Your_Api_Key>")

# Load the Gemini model
model = genai.GenerativeModel("gemini-pro")

def aiProcess(command):
    try:
        response = model.generate_content(command)
        return response.text
    except Exception as e:
        return f"Error from Gemini: {e}"

def processcommand(c):
    if "open youtube" in c.lower():
        speak_old(f"Executing {c}")
        wb.open("https://www.youtube.com/")
    elif "open instagram" in c.lower():
        speak_old(f"Executing {c}")
        wb.open("https://instagram.com")
    elif "open whatsapp" in c.lower():
        speak_old(f"Executing {c}")
        wb.open("https://whatsapp.com")
    elif "open brower" in c.lower():
        speak_old(f"Executing {c}")
        wb.open("https://google.com")
    elif "open edge" in c.lower():
        speak_old(f"Executing {c}")
        wb.open("https://google.com")
    elif c.lower().startswith("play"):
        speak_old(f"Executing {c}")
        try:
            song=c.lower().split(" ")[1]
            link=musiclibrary.music[song]
            wb.open(link)
        except Exception as e:
            speak_old("error in execution")
    elif "file" in c.lower():
        try:
            speak_old(f"opening {c} file")
            if c.lower().endswith("text"):
                os.startfile(f'{c}.txt')
            elif c.lower().endswith("pdf"):
                os.startfile(f'{c}.pdf')
            elif c.lower().endswith("mp3"):
                os.startfile(f'{c}.mp3')
            elif c.lower().endswith("mkv"):
                os.startfile(f'{c}.mkv')
            
        except Exception as e:
            speak_old(f"Error in openging {c} file")
    else:
        output=aiProcess(c)
        speak_old(output)

if __name__=="__main__":
    speak_old("Intializing Friday")
    # m="play fallout"
    # processcommand(m)
    
    while (True):
        r=sr.Recognizer()
        
        #Recognizing the voice of called friday from microphone
        print("recognizing")
        try:
            with sr.Microphone() as source:
                audio=r.listen(source,timeout=5,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if(word.lower() == "friday"):
                speak_old("Yes Boss")
                with sr.Microphone() as source:
                    print("Friday active.....")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)
                    print(command)
                    processcommand(command)
            elif "terminate yourself" in word.lower():
                speak_old("terminating friday")
                break
        except Exception as e:
            print("Error:{0}".format(e))



