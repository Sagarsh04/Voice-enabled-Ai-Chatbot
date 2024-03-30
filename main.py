# import json
# import os
# import pyttsx3
# # import espeak_ng_python
# import time

# import google.generativeai as genai
# from flask import Flask, jsonify, request, send_file, send_from_directory

# # 🔥 FILL THIS OUT FIRST! 🔥
# # 🔥 GET YOUR GEMINI API KEY AT 🔥
# # 🔥 https://g.co/ai/idxGetGeminiKey 🔥
# API_KEY = 'AIzaSyBM0YCnXiWsQrMTn3QS9UKcRKUuQr6ZeM0'

# genai.configure(api_key=API_KEY)

# app = Flask(__name__)


# @app.route("/")
# def index():
#     return send_file('templates/index.html')


# @app.route("/api/generate", methods=["POST"])
# def generate_api():
#     if request.method == "POST":
#         if API_KEY == 'TODO':
#             return jsonify({ "error": '''
#                 To get started, get an API key at
#                 https://g.co/ai/idxGetGeminiKey and enter it in
#                 main.py
#                 '''.replace('\n', '') })
#         try:
#             req_body = request.get_json()
#             content = req_body.get("contents")
#             model = genai.GenerativeModel(model_name=req_body.get("model"))
#             response = model.generate_content(content, stream=True)
#             def stream():
#                 for chunk in response:
#                     yield 'data: %s\n\n' % json.dumps({ "text": chunk.text })

#             return stream(), {'Content-Type': 'text/event-stream'}

#         except Exception as e:
#             return jsonify({ "error": str(e) })


# @app.route('/<path:path>')
# def serve_static(path):
#     return send_from_directory('templates', path)




# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# # print(voices[1].id)
# engine.setProperty('voice', voices[1].id)


# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()


# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour>=0 and hour<12:
#         speak("Good Morning!")

#     elif hour>=12 and hour<18:
#         speak("Good Afternoon!")

#     else:
#         speak("Good Evening!")

#     speak("Sir .. I am Friday ..  How may I help you.")

# def takeCommand():
#     #It takes microphone input from the user and returns string output

#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in') # type: ignore
#         print(f"User said: {query}\n")

#     except Exception as e:
#         # print(e)
#         print("Say that again please...")
#         speak("Say that again please...")
#         return "None"
#     return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('knikhil@gmail.com', 'password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()

# if __name__ == "__main__":
#     wishMe()
#     while True:
#     # if 1:
#         query = takeCommand().lower()

#         # Logic for executing tasks based on query
#         if 'wikipedia' in query:
#             speak('Searching Wikipedia...')
#             query = query.replace("wikipedia" or 'search wikipedia for', "")
#             results = wikipedia.summary(query, sentences=3)
#             speak("According to Wikipedia")
#             print(results)
#             speak(results)

#         elif 'open youtube' in query:
#             webbrowser.open("youtube.com")

#         elif 'open google' in query:
#             webbrowser.open("google.com")

#         elif 'open stackoverflow' in query:
#             webbrowser.open("stackoverflow.com")

#         elif 'play music' in query:
#             music_dir = 'C:\\New folder\\Songs'
#             songs = os.listdir(music_dir)
#             print(songs)
#             os.startfile(os.path.join(music_dir, songs[0]))

#         elif 'the time' in query:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")
#             speak(f"Sir, the time is {strTime}")

#         elif 'open code' in query:
#             codePath = "C:\\Users\\knikh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
#             os.startfile(codePath)

#         elif 'email to Nikhil' in query:
#             try:
#                 speak("What should I say?")
#                 content = takeCommand()
#                 to = "nikhil@gmail.com"
#                 sendEmail(to, content)
#                 speak("Email has been sent!")
#             except Exception as e:
#                 print(e)
#                 speak("Sorry my friend. I am not able to send this email")
        
#         elif 'exit' in query:
#             speak("Thank you for using me")
#             exit()




import json
import os
import time
import datetime
import smtplib
import webbrowser
import speech_recognition as sr
import wikipedia
from gtts import gTTS
from flask import Flask, jsonify, request, send_file,render_template, send_from_directory

import google.generativeai as genai

# 🔥 FILL THIS OUT FIRST! 🔥
# 🔥 GET YOUR GEMINI API KEY AT 🔥
# 🔥 https://g.co/ai/idxGetGeminiKey 🔥
API_KEY = 'AIzaSyBM0YCnXiWsQrMTn3QS9UKcRKUuQr6ZeM0'

genai.configure(api_key=API_KEY)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(('index.html'))

@app.route("/api/generate", methods=["POST"])
def generate_api():
    if request.method == "POST":
        if API_KEY == 'TODO':
            return jsonify({ "error": '''
                To get started, get an API key at
                https://g.co/ai/idxGetGeminiKey and enter it in
                main.py
                '''.replace('\n', '') })
        try:
            req_body = request.get_json()
            content = req_body.get("contents")
            model = genai.GenerativeModel(model_name=req_body.get("model"))
            response = model.generate_content(content, stream=True)
            def stream():
                for chunk in response:
                    yield 'data: %s\n\n' % json.dumps({ "text": chunk.text })

            return stream(), {'Content-Type': 'text/event-stream'}

        except Exception as e:
            return jsonify({ "error": str(e) })

def speak(audio):
    tts = gTTS(text=audio, lang='en')
    tts.save("audio.mp3")
    os.system("mpg123 audio.mp3")  # or any other command-line player

@app.route('/about')
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Sir, I am Friday. How may I help you?")

def takeCommand():
    # It takes microphone input from the user and returns string output
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
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('knikhil@gmail.com', 'password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    app.run(port=int(os.environ.get('PORT', 80)))
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia" or 'search wikipedia for', "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\New folder\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\knikh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to Nikhil' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "nikhil@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")

        elif 'exit' in query:
            speak("Thank you for using me")
            exit()
