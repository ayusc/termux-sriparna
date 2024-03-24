import os
import re
import sys
import subprocess
import random
import string
import time
import pytz
from datetime import datetime
from dateutil import tz
from geopy.geocoders import Nominatim
import speech_recognition as sr
from g4f.client import Client
from g4f.Provider import RetryProvider, Bing, ChatgptAi, OpenaiChat
import json
import python_weather
import asyncio
import g4f.debug
import dialog

g4f.debug.logging = False

client = Client(provider=RetryProvider([ChatgptAi, OpenaiChat, Bing], shuffle=False))

def load_app_mappings(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    else:
        return {}

python_version = "{}.{}".format(sys.version_info.major, sys.version_info.minor)
appjson_path = "/data/data/com.termux/files/usr/lib/python{}/site-packages/sriparna/apps.json".format(python_version)

# Check if the given path exists, if not, fallback to using "apps.json"
if os.path.exists(appjson_path):
    app_mappings = load_app_mappings(appjson_path)
else:
    app_mappings = load_app_mappings("apps.json")

# Generate random 5-character strings for input and output file paths
random_chars = "".join(
    random.choices(string.ascii_letters + string.digits + string.punctuation, k=5)
)
input_file_path = f"/data/data/com.termux/files/home/{random_chars}.amr"
output_file_path = f"/data/data/com.termux/files/home/{random_chars}.wav"
d = dialog.Dialog(dialog="dialog")

def record_audio():
 if os.path.exists(input_file_path):
    os.remove(input_file_path)

 code, tag = d.radiolist(
    "Select an option:",
    choices=[
        ("Start recording", "Start recording", False),
        ("Exit", "Exit", False)
    ],
    height=10,
    width=40,
    no_tags=True,
    no_cancel=True
)

 if code == d.OK:
    if tag == "Start recording":
        d.infobox("Starting recording...")
        subprocess.run(["termux-microphone-record", "-q"], stdout=subprocess.DEVNULL)
        subprocess.run(
            ["termux-microphone-record", "-e", "awr_wide", "-f", input_file_path],
            stdout=subprocess.DEVNULL,
        )
        d.msgbox("Recording finished.")
        
    elif tag == "Exit":
        sys.exit()


def convert_to_wav(input_file, output_file):
    subprocess.run(
        [
            "ffmpeg",
            "-i",
            input_file,
            "-acodec",
            "pcm_s16le",
            "-ac",
            "1",
            "-ar",
            "16000",
            output_file,
            "-y",
            "-loglevel",
            "quiet",
        ]
    )


def recognize_speech(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return "Error: " + str(e)
          
