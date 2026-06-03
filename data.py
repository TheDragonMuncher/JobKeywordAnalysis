import sqlite3
from datetime import datetime
import json

def InitiateConnection():
    connection = sqlite3.connect('Postings.db')
    cursor = connection.cursor()

    if cursor.execute("select name from sqlite_master where name='postings'").fetchone() is None:
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
    if cursor.execute("select name from sqlite_master where name='insights'").fetchone() is None:
        cursor.execute(
            "create table postings (" \
                "posting_id integer references postings(id)," \
                "keywords text," \
                "required text," \
                "nice_to_have text," \
                "seniority text" \
                "analyzed_at datetime" \
            ");"
        )

    return cursor

def WritePostingsToDB(postings: json):
    cursor = InitiateConnection()
    for posting in postings:
        data = [
            posting['title'],
            posting['company_name'],
            posting['source_link'],
            posting['description'],
            datetime.now()
        ]
        cursor.execute("insert into postings values (?,?,?,?,?)",data)
    cursor.connection.commit()


def ReadPostingsFromDB():
    cursor = InitiateConnection()
    results = cursor.execute("select * from postings where analyzed = 0").fetchall()
    return results


def WriteInsightToDB(insight: json):
    cursor = InitiateConnection()
    data = [
        insight['keywords'],
        insight['required'],
        insight['nice_to_have'],
        insight['seniority'],
        datetime.now()
    ]
    cursor.execute("insert into postings values (?,?,?,?,?)",data)
    cursor.connection.commit()


def ReadLastInsightFromDB():
    cursor = InitiateConnection()
    result = cursor.execute("select * from insights").fetchone()
    return result

def ReadAllInsightFromDB():
    cursor = InitiateConnection()
    results = cursor.execute("select * from insights").fetchall()
    return results


"""
https://docs.python.org/3/library/sqlite3.html
"""