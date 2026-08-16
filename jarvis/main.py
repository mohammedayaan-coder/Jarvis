import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from google import genai
from dotenv import load_dotenv
import os
import pywhatkit

 # setup

r = sr.Recognizer()
ttsx = pyttsx3.init()


def speak(text):
    print("Jarvis:", text)

    ttsx.say(text)
    ttsx.runAndWait()

load_dotenv()


client = genai.Client(api_key=os.getenv("APIkey"))



def process_command(c):
    command = c.lower()

 # Command to open websits 

    if command == "open google":
        webbrowser.open("https://google.com")
        speak("opend google")

    elif command == "open youtube":
        webbrowser.open("https://youtube.com")
        speak("opend youtube")

    elif command == "open linkedin":
        webbrowser.open("https://linkedin.com")
        speak("opend linkedin")

    elif command == "open instagram":
        webbrowser.open("https://instagram.com")
        speak("opend instagram")

    elif command == "open github":
            webbrowser.open("https://github.com")
            speak("opend github")

    elif command == "open yt music":
            webbrowser.open("https://music.youtube.com/")
            speak("opend yt music")

    elif command == "open my github profile":
                webbrowser.open("https://github.com/mohammedayaan-coder")
                speak("opend your github profile")

    else:
        processai(command)

def processai(command):

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=command
    )

    answer = response.text
    speak(answer)


if __name__ == "__main__":

    speak("Initializing Jarvis...")

    while True:

        try:
            # Listen for wake word
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)

            word = r.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("hello")
                
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source, timeout=2,phrase_time_limit=2)

                command = r.recognize_google(audio)

                print("Command:", command)
                # message section
                if command.lower() == "send a message":
                    
                    with sr.Microphone() as source:
                        print("Name...")
                        audio = r.listen(source, timeout=5, phrase_time_limit=5)

                    name = r.recognize_google(audio).lower()
                    print("Name:", name)

                    # Get message
                    with sr.Microphone() as source:
                        print("Message...")
                        audio = r.listen(source, timeout=5, phrase_time_limit=10)

                    message = r.recognize_google(audio)
                    print("Message:", message)


                    phone_number = numbers.get(name)

                    if phone_number:
                        speak(f"Sending message to {name}")

                        pywhatkit.sendwhatmsg_instantly(
                            phone_number,
                            message,
                            wait_time=10,
                            tab_close=True,
                            close_time=1
                        )
                    else:
                        speak(f"I don't have a number saved for {name}")
                
                process_command(command)

        except Exception as e:
            print("Error:", e)
