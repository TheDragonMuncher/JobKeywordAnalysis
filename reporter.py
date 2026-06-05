import pandas as pd

import data
import config

def ReportInsights():
    insights = data.ReadAllInsightFromDB()

    keywords = []
    required = []
    nice_to_have = []
    for insight in insights:
        keywords += insight[1].split(',')
        required += insight[2].split(',')
        nice_to_have += insight[3].split(',')

    keywordDf = pd.DataFrame(keywords,columns=['Keywords'])
    keywordDf.drop(keywordDf[keywordDf['Keywords'] == ''].index, inplace=True)

    requiredDf = pd.DataFrame(required,columns=['Required Skills'])
    requiredDf.drop(requiredDf[requiredDf['Required Skills'] == ''].index, inplace=True)

    niceDf = pd.DataFrame(nice_to_have,columns=['Nice to Have Skills'])
    niceDf.drop(niceDf[niceDf['Nice to Have Skills'] == ''].index, inplace=True)

    print(keywordDf.value_counts().head(),'\n')
    print(requiredDf.value_counts().head(),'\n')
    print(niceDf.value_counts().head(),'\n')

ReportInsights()