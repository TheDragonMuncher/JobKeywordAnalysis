import pandas as pd

import data
import config

def ReportInsights():
    insights = data.ReadAllInsightFromDB()
    for insight in insights:
        print(insight,'\n')