import os
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk
# from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer, AudioOutputConfig


# env 저장값 로딩
load_dotenv()

#환경 변수 로딩
speech_config = speechsdk.SpeechConfig(subscription = os.environ.get('KEY')
                                       ,region = os.environ.get('REGION'))

audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker = True)

# 보이스 설정
speech_config.speech_synthesis_voice_name = 'ko-KR-jiMinNeural'
speech_config.synthesizer = speechsdk.SpeechSynthesizer(speech_config = speech_config,audio_config = audio_config)

# 음성으로 변환할 텍스트를 입력 
# 음성으로 변환할 텍스트를 입력 
print("adding your text to convert voice")
text = input()

# Use speak_text_async method and pass the text as an argument
speech_synthesis_result = speech_config.synthesizer.speak_text_async(text).get()

if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("음성으로 변환된 텍스트 [{}]".format(text))