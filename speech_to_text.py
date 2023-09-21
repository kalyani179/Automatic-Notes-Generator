import requests
import time

AUDIO_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"
API_KEY = "28b510a8616a4a758f35452bb692cec8"

headers = {
    'authorization' : API_KEY,
    'content-type' : 'application/json'
}

url = "https://api.assemblyai.com/v2/transcript"
res = requests.post(url,
                    json={'audio_url':AUDIO_URL},
                    headers = headers)
transcript_id = res.json()['id']

while True:
    polling_endpoint = url + "/" + transcript_id
    res = requests.get(polling_endpoint,headers=headers)
    if(res.json()['status'] == 'completed'):
        print(res.json()['text'])
        break
    else:
        time.sleep(60)