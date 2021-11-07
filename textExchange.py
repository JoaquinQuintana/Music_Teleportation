import re
#import geolocation
import pandas as pd
import random 

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
#swapCoordinates("Europe")
#swapCoordinates("Asia")
#swapCoordinates("Australia")