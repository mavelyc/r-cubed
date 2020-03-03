import configparser
from playsound import playsound
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

config = configparser.RawConfigParser()
config.read('config.properties')

api_key = config.get('API', 't2s_key')
api_url = config.get('API', 't2s_url')


authenticator = IAMAuthenticator(api_key)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url(api_url)

with open('speech.mp3', 'wb+') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'compost',
            voice='en-US_AllisonVoice',
            accept='audio/mp3'        
        ).get_result().content)

playsound('speech.mp3')