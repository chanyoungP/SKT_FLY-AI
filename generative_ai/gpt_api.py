import openai 
from dotenv import load_dotenv
import os

load_dotenv() 

openai.api_key = os.environ.get('OPENAI_API_KEY')
openai.azure_endpoint = os.environ.get('OPENAI_API_ENDPOINT')
openai.api_type = os.environ.get('OPENAI_API_TYPE')
openai.api_version = os.environ.get('OPENAI_API_VERSION')



query = '''
Why is a goat climbing a wall?
'''
# 대화형 언어 모델로 대화를 생성 
result = openai.chat.completions.create(
    model = 'dev-model',     # azure 모델 배포시 설정한 이름
    messages = [                    # 대화를 생성하는 인자, 배열로 생성
        {'role':'system','content':'You are a helpful assistant and zoologist'},
        {'role':'user','content': query}, # role system인지 user인지 설정                            # gpt의 정체성(페르소나 설정) 기본은 어시스턴트
    ],
    temperature = 1   # 답변을 T 처럼 하냐 F 처럼 하냐 
)

print(result)
print(result.choices[0].message.content)
