# termux-sriparna
A voice assistant for Termux written in python using [termux-api](https://wiki.termux.com/wiki/Termux:API) and [g4f](https://github.com/xtekky/gpt4free) (GPT4)

With sriparna you can:

1) Call any number ✅
2) Check battery status ✅
3) Send messages ❌
4) Open any app ✅
5) Check whether ✅
6) See current date and time ❌
7) See live location (with google maps link) ❌
8) Read call logs ❌
9) Perform any search ✅
10) Turn Flash on/off ✅
    
More features coming...

**Note: This is a voice assistant and not to be used as a chatbot !**

Leave a like to the repository
It motivates me to keep continue the project.

**PR's are welcomed !!**
**Report Bugs(if any)**

## Requirements:

• [Termux](https://f-droid.org/en/packages/com.termux/)

• [Termux-Api](https://f-droid.org/en/packages/com.termux.api/)

Note: Download these apps from the following official links only.

Do not use playstore version !!

## Installation:

##### Install using pypi

```
pkg update && pkg upgrade -y
pkg install python -y
pip install -U termux-sriparna
```

After using the above commands you can type ```sriparna``` to run the voice assistant.

##### or

1. Clone the GitHub repository:

```
git clone https://github.com/ayusc/termux-sriparna
```

2. Navigate to the project directory:

```
cd termux-sriparna/sriparna
```

3. Run the setup script
   
```
bash setup.sh
```

4. Install the required Python packages from `requirements.txt`:

```
pip install -r requirements.txt
```

5. Run the voice assistant:

```
python sriparna.py
```

## Commands

Each command is assisted with a pattern type:

##### To call any number you can say "hey sriparna call XXXXXXXXXX"

You can also include country code in your query "hey sriparna call plus(country code)******" it will read the number as "+(country code)number"

Besides you can call a number from your contact list just say "sriparna call ayus", "please call ayus2" etc...

Note: In certain cases the speech recognition may not correctly identify the contact name. In such case it's better to spell the letters in the name individually. For example "sriparna please call a y u s", "call a y u s 2" etc...

##### To check battery you can say "sriparna how much is my battery", "tell my battery percentage", "hello what is my battery status", "tell my battery health"

##### To open any application you can say "open whatsapp", "sriparna please open youtube" etc...

You can open chrome, gmail, youtube with this, if you want more applications you need to specify their package names and class name in app.json

You can use [Shortcut Maker](https://play.google.com/store/apps/details?id=rk.android.app.shortcutmaker) to find package name and package names of installed applications.

For pypi installation: You can directly edit the apps.json file with `vi /data/data/com.termux/files/usr/lib/python3.11/site-packages/sriparna/apps.json`

##### To check the current weather conditions you can "hi sriparna whats the weather alike", "tell me the weather forecast", "what is the current weather condition", "how is the weather today"

##### To turn on flashlight you can say "hey please turn on the flash", "flash on", similarly you can say "hey please turn off the flash", "flash off" to turn it off.

##### To know current date and time you can say "what is(or what's) the time", "what is today's date", "what date is today"

# Credits
Thanks to Slash Mark IT for the project idea.
