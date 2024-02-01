import openai 
from dotenv import load_dotenv
import os
import streamlit as st

# setting
load_dotenv() 
openai.api_key = os.environ.get('OPENAI_API_KEY')
openai.azure_endpoint = os.environ.get('OPENAI_API_ENDPOINT')
openai.api_type = os.environ.get('OPENAI_API_TYPE')
openai.api_version = os.environ.get('OPENAI_API_VERSION')


#streamlit 
st.header("Welcome to chan-Poem writer",divider='rainbow')
st.write("Let's write a wonderful Poem with me")

# user info 
name = st.text_input("input writer's name ")
if name: 
    st.write(name + '님 반갑습니다.')
# query = st.text_input('Query : ')
topic = st.text_input('write topic you want')
content = st.text_area('write content of poem...')
btn_flag = st.button("RUN",type='primary')
# 대화형 언어 모델로 대화를 생성 
# result = openai.chat.completions.create(
#     model = 'dev-model',     # azure 모델 배포시 설정한 이름
#     messages = [                    # 대화를 생성하는 인자, 배열로 생성
#         {'role':'system','content':'You are a greate poet'},# gpt의 정체성(페르소나 설정) 기본은 어시스턴트
#         {'role':'user','content': 'The Name of poet is' + name},
#         {'role':'user','content': 'The topic of poet is' + topic},
#         {'role':'user','content': 'The contents of poet is' + content},
#         {'role':'user','content': 'Create greate poem with these information'},                             
#     ],
#     temperature = 1   # 답변을 T 처럼 하냐 F 처럼 하냐 
# )
if btn_flag:
    with st.spinner('loading...'):
    # 대화형 언어 모델로 대화를 생성 
        result = openai.chat.completions.create(
        model = 'dev-model',     # azure 모델 배포시 설정한 이름
        messages = [                    # 대화를 생성하는 인자, 배열로 생성
        {'role':'system','content':'You are a greate poet'},# gpt의 정체성(페르소나 설정) 기본은 어시스턴트
        {'role':'user','content': 'The Name of poet is' + name},
        {'role':'user','content': 'The topic of poet is' + topic},
        {'role':'user','content': 'The contents of poet is' + content},
        {'role':'user','content': 'Create greate poem with these information by korean'},                             
    ],
        temperature = 1   # 답변을 T 처럼 하냐 F 처럼 하냐 
        )
        st.success('Done!')
        st.write(result.choices[0].message.content)
