from anthropic import Anthropic
import data
import config

def Analyze():
    postings = data.ReadPostingsFromDB()
    messages = []
    client = Anthropic()

    for posting in postings:
        message = {
            'posting_id':posting[0],
            'params':{
                'model': 'claude-sonnet-4-6',
                'max-tokens':1024,
                'messages':[{
                    'analyzer-prompt':config.claudePrompt,
                    'posting':posting[4]
                }]
            }
        }
        messages.append(message)
    client.messages.batches.create(
        requests=messages
    )

    