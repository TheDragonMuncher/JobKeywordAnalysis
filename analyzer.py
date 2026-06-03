from anthropic import Anthropic
import time
import json
import data
import config

def Analyze():
    postings = data.ReadPostingsFromDB()
    messages = []
    client = Anthropic(api_key='')

    #build batch requests
    for posting in postings:
        messages.append({
            'posting_id':posting[0],
            'params':{
                'model': 'claude-haiku-4-5',
                'max-tokens':1024,
                'system':config.claudePrompt,
                'messages':[{
                    'role':'user',
                    'content':f'Job Title: {posting[1]}\n\
                    Company: {posting[2]}\n\n\
                    {posting[4]}'
                }]
            }
        })
    
    # create and send batch
    batch = client.messages.batches.create(requests=messages)

    # wait for batch to process
    while True:
        status = batch.processing_status

        if status == 'ended':
            break

        time.sleep(60)
    
    # iterate through results/insights and save to db
    results = client.messages.batches.results(batch.id)
    for result in results:
        if result.result.type == 'succeeded':
            raw = result.result.message.content[0].text
            try:
                insight = json.loads(raw)
                data.WriteInsightToDB(insight)
            except json.JSONDecodeError:
                print(f'Bad json {result.custom_id} : {raw}')
        else:
            print(f'Something went wrong on posting {result.custom_id} : {result.result.error}')