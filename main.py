import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import random
import pyttsx3  # Import pyttsx3 for text-to-speech
import numpy as np

chatStr = ""

# Set up the text-to-speech engine
engine = pyttsx3.init()

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = "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" # Ensure that 'apikey' is defined somewhere in your code
    chatStr += f"Altamash: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def ai(prompt):
    openai.api_key = "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" # Ensure that 'apikey' is defined somewhere in your code
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def say(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])




        def play_music(file_path):
            try:
                os.startfile(file_path)  # Opens the file with the default media player
            except Exception as e:
                print(f"An error occurred: {e}")


        # Directory containing your music files
        music_directory = r"C:\Users\altam\Music"  # Replace with the path to your music directory

        # Get a list of all files in the directory
        music_files = [os.path.join(music_directory, file) for file in os.listdir(music_directory) if
                       file.endswith(".mp3")]

        # Usage
        if "open music" in query:
            for music_path in music_files:
                play_music(music_path)
        # Use 'start' to open the music file with the default player

        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir, the time is {hour} hours and {min} minutes")


        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)
  
        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)
