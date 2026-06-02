import requests
import config
import data
import json

def RetrievePostings():

    response = requests.get(config.serpApiKey, params=config.params)
    responseJson = response.json()['jobs_results']
    data.WriteToDB(responseJson)

RetrievePostings()