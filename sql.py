
import sqlite3
import csv

def create(self):
    dataBaseName = self + '.db'
    conn = sqlite3.connect(dataBaseName)
    cur = conn.cursor()
    
    #Build tables
    cur.execute("""CREATE TABLE IFRAME(
        mood TEXT,
        Playlist TEXT,
        iframe TEXT 
        
    )""")
    #make sure to commit and close               
    conn.commit()
    conn.close()  

def fillDB(name,tableName):
    dbName = name + '.db'
    con = sqlite3.connect(dbName)
    cur = con.cursor()

    a_file = open('Spotify Mood iframes.csv')
    rows = csv.reader(a_file)
    cur.executemany("INSERT INTO IFRAME VALUES (?, ?, ?)", rows)

    cur.execute("SELECT * FROM IFRAME")
    rows = cur.fetchall()
    #for row in rows:
    #    print('Row in table ' + tableName + ' in database ' + dbName ,row,'\n')

    con.commit()
    con.close() 

#create('iframe')
fillDB('iframe','IFRAME')