import re
import geolocation

def swapCoordinates(country):
    #get coordinates for country requested
    x = geolocation.GetCoordinates(country)

    #swap old coordinates with new ones
    with open("templates/index.html", 'r+') as f:
        text = f.read()
        replacement = 'fromLonLat('+str(x[:-1])+')'
        print(replacement)
        text = re.sub(r'fromLonLat\(.*?\)',replacement, text)
        f.seek(0)
        f.write(text)
        f.truncate()