# Conversational app

This is the first version of the conversational app.

## Running the App

To run this locally, you will need an OpenAI api key for the free version (gpt 3.5).

Create a file at audio_app/.env with the following lines:

```
export OPENAI_API_KEY=one-api-key
```

Now open a Console, go to `audio_app` folder (`cd audio_app` from `conversational-app`) and run:

```
cd audio_app
python -m venv env
source env/bin/activate
pip install -r requirements.txt
source .env
python manage.py migrate
python manage.py runserver
```

This will create the `db.sqlite3` file for the database, to store AudioResponse objects that collect the transcription of the audio and the text response that the LLM generated.

Go to `http://127.0.0.1:8000/` and you can start using the app as a user.

## Deploying

One easy and fast way to deploy is using [ngrok](https://ngrok.com/) . Follow the steps to install and have it running.
That will expose your local host and port into the public web, and it will give you a public url where you can reach your local app from outside.
Add the line `export PROD_URL=https://NGROK-ID.ngrok-free.app/` to the .env file, re-run `source .env`, and re-run the app. You should be ready to access the `ngrok` public url and have it working properly.

## Basic steps the App does

The app works with the following steps:

- User loads the frontend.
- The frontend creates a Websocket communication with the backend.
- The user records an audio by click on a button to start and stop.
- The frontend sends the audio to the backend in form of bytes, and the Websocket connection stays alive waiting for the response.
- The backend receives the audio and transcribes it to text using Whisper.
- It sends the transcription to GPT for it to generate a response according to some laid instructions.
- The backend uses gTTS for text-to-speech generation.
- It sends the audio that was generated with LLM's response to the frontend.
- The frontend receives the audio and automatically plays it to the user, allowing them to re-play it, change its speed and download it.

## Possible future improvements

*This App was created in 4 hours as part of an interview process.* Future improvements include:

- Add a configuration so that it's easy to change between libraries and models used, for the 3 main parts of the app: speech-to-text (currently Whisper), LLM response (currently GPT 3.5 with locally installed apikey), and text-to-speech (currently gTTS always in English).

- Allow the app to be always recording (make the button unnecessary) and send bytes once it hears something transcribable, making use of the Websocket async communication.

- Test different voices, tones and existing libraries so that the audio for the user is as human-sounding as possible.

- Add tests for the backend.

- Store more information in the database, like time spent in each process, audio files, and data about the user's identity.

- PostgreSQL for production instead of SQLite.