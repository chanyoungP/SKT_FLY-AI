import os
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk
# from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer, AudioOutputConfig


# env 저장값 로딩
load_dotenv()

# #환경 변수 로딩
# speech_config = speechsdk.SpeechConfig(subscription = os.environ.get('KEY')
#                                        ,region = os.environ.get('REGION'))

# audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker = True)

# # 보이스 설정
# speech_config.speech_synthesis_voice_name = 'ko-KR-jiMinNeural'
# speech_config.synthesizer = speechsdk.SpeechSynthesizer(speech_config = speech_config,audio_config = audio_config)

import os
import azure.cognitiveservices.speech as speechsdk

def speech_to_text():
    # Azure 서비스 키 및 지역 정보
    speech_key = os.environ.get('KEY')
    speech_region = os.environ.get('REGION')

    # Speech SDK 설정
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)

    # 오디오 입력 설정 (마이크 사용)
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

    # SpeechRecognizer 생성
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Listening for speech... Press Ctrl+C to exit.")

    # 실시간 음성 입력 처리
    result = speech_recognizer.recognize_once()

    # 결과 확인
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))

if __name__ == "__main__":
    speech_to_text()
