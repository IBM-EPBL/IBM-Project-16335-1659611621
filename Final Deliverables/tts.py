from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
authenticator = IAMAuthenticator('NF0qqePBq845-q9DzSz-fdFMGfr7kvKxILoxBykOnlbX')
text_to_speech = TextToSpeechV1( authenticator=authenticator
)
text_to_speech.set_service_url('https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/f4c57d17-ac42-458a-8552-cf3a0baa9ca7')
with open('hello_world.wav', 'wb') as audio_file: audio_file.write( text_to_speech.synthesize(
'its time to take insulin',
 
voice='en-US_AllisonV3Voice', accept='audio/wav'
).get_result().content)
