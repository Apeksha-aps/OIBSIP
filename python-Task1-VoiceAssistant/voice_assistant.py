# Project: Voice asistant (OIBSIP - python Programming Task 1)
# Authur: Apeksha Suhas Phapale
import speech_recognition as sr 
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
            print("Recognizing...")
            command = recognizer.recognize_google(audio, language='en-in')
            print(f"You said: {command}")
            return command.lower()
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
            return ""
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that. Please repeat.")
            return ""
        except sr.RequestError:
            speak("Network error. Please check your internet connection.")
            return ""

def run_assistant():
    speak("Hello Apeksha! I am your Python Voice Assistant. How can I help you today?")
    
    while True:
        command = listen()
        
        if not command:
            continue
            
        if "hello" in command or "hi" in command:
            speak("Hello! Nice to meet you. What would you like me to do?")
            
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")
            
        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {current_date}")
            
        elif "search" in command:
            speak("What should I search for?")
            query = listen()
            if query:
                speak(f"Searching Google for {query}")
                url = f"https://google.com/search?q={query}"
                webbrowser.open(url)
                
        elif "exit" in command or "stop" in command or "bye" in command:
            speak("Goodbye Apeksha! Have a great day.")
            break
            
        else:
            speak("You can ask me to say hello, tell the time or date, search something, or say exit to stop.")

if __name__ == "__main__":
    run_assistant()
