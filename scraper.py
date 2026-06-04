import requests
import config
import data

def RetrievePostings():
    response = requests.get('https://serpapi.com/search?engine=google_jobs', params=config.params)
    responseJson = response.json()['jobs_results']
    data.WriteToDB(responseJson)