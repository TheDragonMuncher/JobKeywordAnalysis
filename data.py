import sqlite3
import datetime

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

def WriteToDB(postings):
    cursor = InitiateConnection()
    for posting in postings:
        data = [
            posting['title'],
            posting['company_name'],
            posting['source_link'],
            posting['description'],
            datetime.datetime.now()
        ]
        cursor.execute("insert into postings values (?,?,?,?,?)",data)


def ReadFromDB():
    return asdf



"""
https://docs.python.org/3/library/sqlite3.html
"""