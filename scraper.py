import requests
import config
import data
import json

def RetrievePostings():

    params = {
        'q':'Junior Software Developer',
        'location':'Waterdown',
        'api_key':'4283f57cada3ed115775418dff33d2550933323a2809c4429f07eaa2a7fb2ec7'
    }
    response = requests.get(config.serpApiKey, params=params)
    responseJson = response.json()
    with open('sampe_output.json', 'w') as file:
        json.dump(responseJson, file)

RetrievePostings()