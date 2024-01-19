from flask import Flask, url_for, request, render_template, session
import requests , os , json, uuid
from dotenv import load_dotenv

# env load
load_dotenv()

#app
app = Flask(__name__)

# adding path 
@app.route('/',methods = ['GET'])

def index():
    return render_template('index.html')

@app.route('/', methods = ['POST'])

def index_post():
    original_txt = request.form['text']
    target_language = request.form['language']

    #key laod 
    key = os.environ['TR_KEY']
    location = os.environ['TR_LOCATION']
    end_point = os.environ["END_POINT"]

    # translator api version setting
    path = '/translate?api-version=3.0'

    target_language_parameter = '&to=' + target_language

    full_url = end_point + path + target_language_parameter

    #
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceid': str(uuid.uuid4())
    }

    #
    body = [{'text': original_txt}]

    #
    translator_request = requests.post(full_url,headers=headers,json=body)

    #
    translator_response = translator_request.json()

    #
    translated_txt = translator_response[0]['translations'][0]['text']

    return render_template(
        'results.html',
        translated_txt = translated_txt,
        original_txt = original_txt,
        target_language = target_language
    )

if __name__ == '__main__':
    app.run('0.0.0.0', port=8080)