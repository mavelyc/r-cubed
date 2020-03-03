from playsound import playsound
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


authenticator = IAMAuthenticator('oxk4HiUC_71bklt-LTrkacNlGvXqAxLdewYRWtjsAHSH')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/4f92beff-8135-4c48-bb39-83726add4b58')

with open('speech.mp3', 'wb+') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'compost',
            voice='en-US_AllisonVoice',
            accept='audio/mp3'        
        ).get_result().content)

playsound('speech.mp3')