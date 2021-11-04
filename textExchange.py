import re
import geolocation

x = geolocation.GetCoordinates('honolulu')
#print(x)

with open("index.html", 'r+') as f:
    text = f.read()
    replacement = 'fromLonLat('+str(x[:-1])+')'
    print(replacement)
    text = re.sub(r'fromLonLat\(.*?\)',replacement, text)
    f.seek(0)
    f.write(text)
    f.truncate()