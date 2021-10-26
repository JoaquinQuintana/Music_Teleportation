#changing python env to anaconda: https://medium.com/@udiyosovzon/how-to-activate-conda-environment-in-vs-code-ce599497f20d

from geopy.geocoders import Nominatim

def GetCoordinates(EnterLocation):
    # calling the Nominatim tool
    loc = Nominatim(user_agent="GetLoc")
    
    # entering the location name
    getLoc = loc.geocode(EnterLocation)
    
    # printing address
    print(getLoc.address, '\n')

    # printing latitude and longitude
    print("Latitude = ", getLoc.latitude, "\n")
    print("Longitude = ", getLoc.longitude)

#GetCoordinates('Rocky Ford Colorado')
#GetCoordinates('Boulder Colorado')
#GetCoordinates('honolulu hi')
#GetCoordinates('honolulu')
GetCoordinates('North Korea')