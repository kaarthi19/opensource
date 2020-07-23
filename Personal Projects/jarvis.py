from gtts import gTTS #or use pyttsx3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pygame import mixer

import speech_recognition as sr
import re
import time
import webbrowser
import random
import smtplib
import requests
import urllib.request
import urllib.parse
import bs4
import datetime

def talkJarvis(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        text_to_speech = gTTS(text=audio, lang='en-uk')
        text_to_speech.save('audio.mp3')
        mixer.init()
        mixer.music.load('audio.mp3')
        mixer.music.play()


def myCommand():
    "listens for commands"
    #initializing the recognizer
    #to recognise speech

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Jarvis is ready...')
        r.pause_threshold = 1
        #waits for a second to let the recognizer adjust the
        #energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source, duration=1)
        #listens for the user's input
        audio = r.listen(source)
        print('analyzing...')

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
        time.sleep(2)

    #loop back if the command can't be heard
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command


def jarvis(command):
    errors=[
        "I don't know what you mean",
        "Excuse me?",
        "Can you repeat it please?",
    ]
    """if statements for executing commands"""

    # Search on Google
    if 'open google and search' in command:
        reg_ex = re.search('open google and search (.*)', command)
        search_for = command.split("search",1)[1]
        print(search_for)
        url = 'https://www.google.com'
        if reg_ex:
            subgoogle = reg_ex.group(1)
            url = url + 'r/' + subgoogle
        talkJarvis('Okay!')
        driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        driver.get('https://www.google.com')
        search = driver.find_element_by_name('q')
        search.send_keys(str(search_for))
        search.send_keys(Keys.Return) #hits return for search

    #send email
    elif 'email' in command:
        talkJarvis('Who would you like to send this email?')
        recipient = myCommand()

        if 'university email' in recipient:
            email_address = 'kaarthigeswaran@gmail.com'
            email_password = 'text' #leaving empty for privacy concerns
            talkJarvis('What you would like to say in the email')
            content = myCommand()
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login(email_address, email_password)
            mail.sendmail('sender_email', 'receiver_email', content) #will update with a dictionary/list of contacts
            mail.close()
            talkJarvis('Email has been sent successfully.')

        else:
            talkJarvis('I don\'t know what you mean!')
            continue

#search in wikipedia (e.g. Can you search in wikipedia apples)
    elif 'wikipedia' in command:
        reg_ex = re.search('wikipedia (.+)', command)
        if reg_ex:
            query = command.split("wikipedia",1)[1]
            response = requests.get("https://en.wikipedia.org/wiki/" + query)
            if response is not None:
                html = bs4.BeautifulSoup(response.text, 'html.parser')
                title = html.select("#firstHeading")[0].text
                paragraphs = html.select("p")
                for para in paragraphs:
                    print(para.text)
                intro = '\n'.join([para.text for para in paragraphs[0:3]])
                print(intro)
                mp3name = 'speech.mp3'
                language = 'en'
                myobj = gTTS(text=intro, lang=language, slow=False)
                myobj.save(mp3name)
                mixer.init()
                mixer.music.load("speech.mp3")
                while mixer.music.play()
    elif 'stop' in command:
        mixer.music.stop()

#search videos on Youtube

    elif 'youtube' in command:
        talk('OK!')
        reg_ex = re.search('youtube (.+)', command)
        if reg_ex:
            domain = command.split("youtube",1)[1]
            query_string = urllib.parse.urlencode({"search_query" : domain})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            print("http://www.youtube.com/watch?v=" + search_results[0])
            webbrowser.open("http://www.youtube.com/watch?v={}".format(search_results[0]))
            pass

    #time
    elif 'time' in command:
        now = datetime.datetime.now()
        talkJarvis('It is %d %d' %(now.hour, now.minute))

    #conversation
    elif 'hello' in command:
        talk('Hello! I am Jarvis. How can I help you?')
        time.sleep(3)
    elif 'who are you' in command:
        talk('I am an intelligent personal assistant designed to assist you on your daily matters')
        time.sleep(3)
    elif 'Jarvis stands for' or 'Jarvis meaning' or 'meaning of Jarvis' in command:
        talk('My name is an abbreviation that stands for Just A Rather Very Intelligent System')
        time.sleep(3)
    elif 'who created you' or 'why you were created' in command:
        talk('Mr Kaarthigeswaran created me to assist him with his daily affairs and also demonstrate how powerful Python can be')

    else:
        error = random.choice(errors)
        talk(error)
        time.sleep(3)


while True:
    time.sleep(4)
    jarvis(myCommand())
