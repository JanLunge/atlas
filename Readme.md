![header](./assets/orbit-header.png)
<h1 align="center">Orbit
</h1>
<h4 align="center">
a modular platform for building a voice based LLM assistant</h4>
<p align="center">
    <a href="https://github.com/JanLunge/orbit/stargazers"><img src="https://img.shields.io/github/stars/JanLunge/orbit" alt="Stars Badge"/></a>
    <a href="https://github.com/JanLunge/orbit/network/members"><img src="https://img.shields.io/github/forks/JanLunge/orbit" alt="Forks Badge"/></a>
</p>

# services
* ⚙️ Command service for custom executable commands
* ❗️ Hotword detection with porcupine
* 🧠 LLM AI integration with OpenAi or local inference
* 🎧 whisper speech recognition
* 🎤 audio streaming via mqtt (audio_satelite)
* 💬 TTS via elevenlabs or pyttsx3

![demo](./assets/demo-shell.gif)

## what is this?
Build your own jarvis or alexa/siri/google assistant with this modular platform. 
it will listen for audio with a microphone streamer via mqtt, 
then a hotword module will trigger the hotword event if you say the hotword/wakeword atlas
then the audio will be streamed to a whisper speech recognition module that will return the text
then the text will be sent to an AI module that will return a response
then the text will be sent to a command module that will execute the command
then the response will be sent to a TTS module that will speak the response

This has been tested on an m1 mac

## TODOs:
- [ ] implement function calling in the ai module so the ai can trigger commands
- [ ] create a management interface for the function calling
- [ ] support local inference with custom models

current token limitations make the function calling not really feasible but in the close future you will be able to use your computer or other api apps just with your voice,
AI will be the interface between you and your computer. get in now and be ready for the future!

# requirements
- a Mqtt server

on OSX install one with `brew install mosquitto` then manage it with `brew services start mosquitto`
and 
`brew services stop mosquitto`
* `ffmpeg` for the whisper speech recognition
* a working `pyaudio` installation

# optional
- openai api key into .env named OPENAI_API_KEY (if you use chatgpt in th eai.py file)
- a porcupine hotword model and access key
- an elevenlabs api key for tts ()



# Setup
1. get a poetry shell with `poetry shell`
2. install the dependencies with `poetry install`
3. then run `python3 main.py` to start the program