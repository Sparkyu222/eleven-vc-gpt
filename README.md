# Eleven-vc-gpt

I was bored and I tried to mix Eleven Labs's API with Open AI's one so I could make a personnal assitant with my voice. I'm still trying to learn Python, so the script might be a little bit janky.

I only tested this script with Python 3.11.

## Setting up
First, copy the `.env-placeholder` file and rename it `.env`. In the copied file, you need to enter the following informations :
```json
{
	"openai": "YOUR OPENAI API KEY HERE",
	"gpt-model": "OPENAI LLM MODEL",
	"elevenlabs": "YOUR ELEVENLABS API KEY HERE",
	"voiceID": "THE ID OF THE VOICE OF YOUR CHOICE FROM ELEVENLABS"
}
```
To obtain the ID of the voice you want to hear, [fetch the voices list from ElevenLabs's API](https://api.elevenlabs.io/docs#/voices/Get_voices_v1_voices_get).

Then install the following requirements via `pip`:
```bash
$ pip install openai elevenslabs
```
And now, you're settled!

## Run
To start your assistant, just launch the following script:

```bash
$ python main.py
```

This will initiate a basic turn-by-turn conversation with your assistant. After a few seconds — the time taken for ElevenLabs' API to infer and transfer the audio data — the voice of your choice will read ChatGPT's response.
