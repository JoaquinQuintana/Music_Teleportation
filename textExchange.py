import pandas as pd
import random
import re

def swapCoordinates(nation):
    #read file with coordinates stored in it
    df = pd.read_pickle("Country_Long_Lat.pkl")
    df = df.set_index('continent')
    df = df[df.index.str.startswith(nation)]
    x = '['+str(float(df['longit'].to_numpy())) + ', ' + str(float(df['latit'].to_numpy()))+']'

    #swap old coordinates with new ones
    with open("templates/index.html", 'r+') as f:
        text = f.read()
        replacement = 'fromLonLat('+str(x)+')'
        text = re.sub(r'fromLonLat\(.*?\)',replacement, text)
        f.seek(0)
        f.write(text)
        f.truncate()
    return x

def getCurrentCorrdinates():
    with open("templates/index.html", 'r+') as f:
        text = f.read()
        current_text = re.findall(r'fromLonLat\(.*?\)',text)
        return current_text

def getIframe(moodSelected,nation):
    df  = pd.read_csv('Moods_Countries.csv', names= ["nation","mood","iframe",'junk'],sep='{', header = None)
    df = df.drop(columns=['junk'])
    #select the mood and country from the dataframe
    df = df[(df["mood"]== moodSelected) & (df["nation"]==nation)]
    print(moodSelected,nation,df)

    #return the iframe for the country and mood provided
    return df.iframe.item()

def exchangeIframe(mood,nation):
    #iframe returned which is related to the mood and nation
    newIframe = getIframe(mood,nation)

    with open("templates/index.html", 'r+') as f:

        text = f.read()
        text = re.sub(r'(?:<iframe[^>]*)(?:(?:\/>)|(?:>.*?<\/iframe>))',newIframe, text)
        f.seek(0)
        f.write(text)
        f.truncate()

    with open("templates/result.html", 'w') as f:
        f2 = open("templates/index.html", 'r+')
        contents = f2.readlines()
        print("!!!!", contents)
        contents.insert(111, "<style> body: {background: url('../static/prague.jpg');} </style>")
        contents = "".join(contents)
        f.write(contents)
        f.close()

def text_exchange(mood,nation):
    #user enters nothing - randomly select from continents or mood
    if not nation:
        l = ['Asia','Africa','Europe','Australia','North America','South America']
        nation = random.choice(l)
    if not mood:
        l = ['Happy','Mellow','Energetic','Chill']
        mood = random.choice(l)

    #exchange both coordinates and the playlist for mood based on users request
    exchangeIframe(mood,nation)
    swapCoordinates(nation)
