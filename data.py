import sqlite3
from datetime import datetime
import json

def InitiateConnection():
    connection = sqlite3.connect('Postings.db')
    cursor = connection.cursor()

    tables = cursor.execute("select name from sqlite_master").fetchall()

    if ('postings',) not in tables:
        cursor.execute(
            "create table postings (" \
                "id integer primary key," \
                "title text," \
                "company text," \
                "source text," \
                "description text," \
                "fetched_at datetime," \
                "analyzed boolean default 0" \
            ");"
        )
    if ('insights',) not in tables:
        cursor.execute(
            "create table insights (" \
                "posting_id integer references postings(id)," \
                "keywords text," \
                "required text," \
                "nice_to_have text," \
                "seniority text," \
                "analyzed_at datetime" \
            ");"
        )

    return cursor

def WritePostingsToDB(postings: json):
    cursor = InitiateConnection()
    data = []
    for posting in postings:
        data.append({
            'title':posting['title'],
            'company':posting['company_name'],
            'source':posting['source_link'],
            'description':'description',
            'fetched_at':datetime.now()
        })
    data = tuple(data)
    cursor.executemany("insert into postings (title,company,source,description,fetched_at) " \
    "values (:title,:company,:source,:description,:fetched_at)",data)

    cursor.connection.commit()
    cursor.connection.close()


def ReadPostingsFromDB():
    cursor = InitiateConnection()
    results = cursor.execute("select * from postings where analyzed = 0").fetchall()
    cursor.connection.close()
    return results

def UpdatePostingsAnalyzedBool():
    cursor = InitiateConnection()
    postings = cursor.execute("update postings set analyzed = 1 where analyzed = 0")
    cursor.connection.close()
    

def WriteInsightToDB(insight: json):
    cursor = InitiateConnection()
    keywords = ''
    required = ''
    nice_to_have = ''

    for item in insight['keywords']:
        keywords += (item + ',')
    for item in insight['required_skills']:
        required += (item + ',')
    for item in insight['nice_to_have_skills']:
        nice_to_have += (item + ',')
    
    data = {
        'keywords':keywords,
        'required':required,
        'nice_to_have':nice_to_have,
        'seniority':insight['seniority_level'],
        'analyzed_at':datetime.now()
    }
    cursor.execute("insert into insights (keywords,required,nice_to_have,seniority,analyzed_at)" \
                   "values (:keywords,:required,:nice_to_have,:seniority,:analyzed_at)",data)
    cursor.connection.commit()
    cursor.connection.close()


def ReadLastInsightFromDB():
    cursor = InitiateConnection()
    result = cursor.execute("select * from insights").fetchone()
    cursor.connection.close()
    return result

def ReadAllInsightFromDB():
    cursor = InitiateConnection()
    results = cursor.execute("select * from insights").fetchall()
    cursor.connection.close()
    return results


"""
https://docs.python.org/3/library/sqlite3.html
"""