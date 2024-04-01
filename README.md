# termux-sriparna

![logo](https://raw.githubusercontent.com/ayusc/termux-sriparna/main/logo.png)

[![Pylint](https://github.com/ayusc/termux-sriparna/actions/workflows/pylint.yml/badge.svg?branch=main)](https://github.com/ayusc/termux-sriparna/actions/workflows/pylint.yml)
[![CodeQL](https://github.com/ayusc/termux-sriparna/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/ayusc/termux-sriparna/actions/workflows/github-code-scanning/codeql)
[![CodeFactor](https://www.codefactor.io/repository/github/ayusc/termux-sriparna/badge)](https://www.codefactor.io/repository/github/ayusc/termux-sriparna)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/ce3bdaaca6014fc5b74bb171e8517b48)](https://app.codacy.com/gh/ayusc/termux-sriparna/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Python>=3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Package Version](https://img.shields.io/pypi/v/termux-sriparna.svg)](https://pypi.python.org/pypi/termux-sriparna/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A voice assistant for Termux written in python using [Termux Api](https://wiki.termux.com/wiki/Termux:API)

With sriparna you can:

1) Call any number ✅
2) Check battery status ✅
3) Send messages ❌
4) Open any app ✅
5) Check whether ✅
6) See current date and time ✅
7) See live location (with google maps link) ❌
8) Read call logs ❌ (Deprecated)
9) Perform any search ✅
10) Turn Flash on/off ✅
    
More features coming...

**Note: This is a voice assistant and not to be used as a chatbot !**

If you like the project, don't forget to leave a star ⭐ to the repository.
It motivates me to keep continue the project.

**PR's are welcomed !!**
**Report Bugs(if any)**

## Requirements:

• [Termux](https://github.com/termux/termux-app/actions)

• [Termux-Api](https://github.com/termux/termux-api/actions)

• [Termux-Widget](https://github.com/termux/termux-widget/actions) (Optional: For shortcut application)

Note: Download these apps from their official github builds only.

Do not use playstore or Fdroid version !!

**Please grant all permission to Termux-api and disable battery optimisation for the app beforehand.** 

## Installation:

##### Install using pypi

```
pkg update -y && pkg upgrade -y
pkg install python -y
pip install -Uv termux-sriparna
```

After using the above commands you can type ```sriparna``` or ```sriparna-gui``` to run the voice assistant.


##### or

1. Clone the GitHub repository:

```
git clone https://github.com/ayusc/termux-sriparna
```

2. Navigate to the project directory:

```
cd termux-sriparna
```

3. Run the setup script
   
```
bash setup.sh
```

4. Run the voice assistant:

```
python sriparna/sriparna.py 
```
For terminal version 

**or**

```
python sriparna/sriparna_gui.py 
```
For gui version

**How to setup shortcut application ?**

![widget](https://raw.githubusercontent.com/ayusc/termux-sriparna/main/demo/widget.gif)

## Commands

Each command is assisted with a pattern type:

##### To call any number you can say "please call XXXXXXXXXX"

You can also include country code in your query "hey call plus(country code)******" it will read the number as "+(country code)number"

Besides you can call a number from your contact list just say "can you call ayus", "please call ayus2" etc...

Note: In certain cases the speech recognition may not correctly identify the contact name. In such case it's better to spell the letters in the name individually. For example "please call a y u s", "call a y u s 2" etc...

##### To check battery you can say "how much is my battery", "tell my battery percentage", "hello what is my battery status", "tell my battery health"

##### To open any application you can say "open whatsapp", "can you open youtube" etc...

You can open chrome, gmail, youtube and whatsapp with this, if you want more applications you need to specify their package names and class name in app.json

You can use [Shortcut Maker](https://play.google.com/store/apps/details?id=rk.android.app.shortcutmaker) to find package name and class names of installed applications.

For pypi installation: You can directly edit the apps.json file with `vi /data/data/com.termux/files/usr/lib/python$(python -c 'import sys; print(sys.version_info[0])').$(python -c 'import sys; print(sys.version_info[1])')/site-packages/sriparna/apps.json
`

##### To check the current weather conditions you can "hi whats the weather alike", "tell me the weather forecast", "what is the current weather condition", "how is the weather today"

##### To turn on flashlight you can say "hey please turn on the flash/torch", "flash/torch on", similarly you can say "hey please turn off the flash/torch", "flash/torch off" to turn it off.

##### To know current date and time you can say "what is(or what's) the time", "what is today's date", "what date is today"

# Credits
[xtekky](https://github.com/xtekky) for [g4f](https://github.com/xtekky/gpt4free)

Slash Mark IT for the project idea.
