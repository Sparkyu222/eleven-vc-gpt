from openai import OpenAI
from elevenlabs import play, stream, save, Voice
from elevenlabs.client import ElevenLabs
import sys
import json
import threading



## OPEN ".ENV" FILE TO GET API KEYS

try:
    envFile = open('.env', "r").read()
except:
    print('Error while trying to open .env file (did you copy the .env file?).')
    exit(False)

try:
    env = json.loads(envFile)
except:
    print("Can't decode JSON data in .env file")
    exit(False)



## SETTING API KEYS

client = OpenAI(
    api_key=env["openai"]
    )

ttsClient = ElevenLabs(
    api_key=env["elevenlabs"]
)

## FUNCTIONS DEFINITION

def txtToSpeech(txt):
    audio = ttsClient.generate(text=txt, voice=Voice(voice_id=env['voiceID']), model="eleven_multilingual_v2", stream=True)
    stream(audio)



## MAIN

while True:

    msg = input("Me : ")

    completion = client.chat.completions.create(
        model = env["gpt-model"],
        messages = [
            {"role": "system", "content": "You are a helpful assistant, you will only respond with short sentences"},
            {"role": "user", "content": msg}
        ],
        temperature=0.8,
        stream=True
    )

    output = ""

    print("ChatGPT : ", end='')

    for chunk in completion:
        if chunk.choices[0].finish_reason == "stop":
            print("")
            continue

        print(chunk.choices[0].delta.content, end='')
        output += chunk.choices[0].delta.content
        sys.stdout.flush()

    thr = threading.Thread(target=txtToSpeech, args=(output,))
    thr.start()