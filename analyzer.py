from anthropic import Anthropic
import time
import json
import data
import config

def Analyze():
    postings = data.ReadPostingsFromDB()
    data.UpdatePostingsAnalyzedBool()
    messages = []
    client = Anthropic(api_key=config.CLAUDE_API_KEY)

    #build batch requests
    for posting in postings:
        messages.append({
            'custom_id':str(posting[0]),
            'params':{
                'model': 'claude-haiku-4-5',
                'max_tokens':1024,
                'system':config.claudePrompt,
                'messages':[
                    {
                        'role':'user',
                        'content':f"Job Title: {posting[1]}\nCompany: {posting[2]}\n\n{posting[4]}"
                    }
                ]
            }
        })
    
    # create and send batch
    batch = client.messages.batches.create(requests=messages)
    batch_id = batch.id

    # wait for batch to process
    while True:
        batch = client.messages.batches.retrieve(batch_id)
        status = batch.processing_status
        print(status)

        if status == 'ended' or status == 'canceled':
            break

        time.sleep(60)
    
    # iterate through results/insights and save to db
    results = client.messages.batches.results(batch.id)
    for result in results:
        if result.result.type == 'succeeded':
            raw = result.result.message.content[0].text
            raw = raw.replace('`','')
            raw = raw.replace('json','')
            raw = raw.replace('\n','')
            try:
                insight = json.loads(raw)
                data.WriteInsightToDB(insight)
            except json.JSONDecodeError:
                print(f'Bad json {result.custom_id} : {raw}')
        else:
            print(f'Something went wrong on posting {result.custom_id} : {result.result.error}')