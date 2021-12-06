#import geolocation
import iframeManager
import pandas as pd
import random 
import re

def swapCoordinates(nation):
    #get coordinates for country requested
    #x = geolocation.GetCoordinates(nation)
    #print(str(x[:-1]))

    #user enters nothing so randomly select from continents
    if not nation:
        l = ['Asia','Africa','Europe','Australia','North America','South America']
        nation = random.choice(l)
        
    df = pd.read_pickle("Country_Long_Lat.pkl")
    df = pd.read_pickle("Country_Long_Lat.pkl")
    df = df.set_index('continent')
    df = df[df.index.str.startswith(nation)]
    x = '['+str(float(df['longit'].to_numpy())) + ', ' + str(float(df['latit'].to_numpy()))+']'
    #print(x)
    #swap old coordinates with new ones
    with open("templates/index.html", 'r+') as f:
        text = f.read()
        replacement = 'fromLonLat('+str(x)+')'
        #print('replacement',replacement)

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

def exchangeIframe(mood,nation):
    #if no mood is provide pick one for them 
    """ if not mood:
        l = ['Happy','Mellow','Energetic','Chill']
        mood = random.choice(l) """
    
    newIframe = iframeManager.getIframe(mood,nation)
    #print(newIframe)
    #get current iframe 
    with open("templates/index.html", 'r+') as f:
        text = f.read()
        text = re.sub(r'(?:<iframe[^>]*)(?:(?:\/>)|(?:>.*?<\/iframe>))',newIframe, text)
        f.seek(0)
        f.write(text)
        f.truncate() 

def text_exchange(mood,nation):
        #user enters nothing so randomly select from continents
    if not nation:
        l = ['Asia','Africa','Europe','Australia','North America','South America']
        nation = random.choice(l)
    if not mood:
        l = ['Happy','Mellow','Energetic','Chill']
        mood = random.choice(l)
    
    
    #exchange both coordinates and the playlist for mood when requested
    exchangeIframe(mood,nation)
    swapCoordinates(nation)

#exchangeIframe('Energetic')
#swapCoordinates("Europe")
#swapCoordinates("Asia")
#swapCoordinates("Australia")