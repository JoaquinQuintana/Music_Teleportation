#changing python env to anaconda: https://medium.com/@udiyosovzon/how-to-activate-conda-environment-in-vs-code-ce599497f20d
from geopy.geocoders import Nominatim
import random
import pandas as pd

def GetCoordinates(EnterLocation):
    """returns coordinates [lat,long,address] when provided a geograhpic location as a string.
    
    Parameters: input type string. 
    
    Returns: tpye list with longitude and latitude,i.e., [long,lat]
        
    Note:This function is for finding geolocations for open layers map

    """
    #user enters nothing so randomly select from continents
    if not EnterLocation:
        l = ['Asia','Africa','Europe','Australia','North America','South America']
        EnterLocation = random.choice(l)
        
    # calling the Nominatim tool
    loc = Nominatim(user_agent="GetLoc")
    
    # entering the location name
    getLoc = loc.geocode(EnterLocation)
    
    # return found address
    #print(getLoc.address, '\n')

    return [EnterLocation,getLoc.longitude,getLoc.latitude]


#create a file to store this information as some computers are not finding the SSL file 
l = ['Asia','Africa','Europe','Australia','North America','South America']
dat = []
for i in l:
    #print(i)
    dat.append(GetCoordinates(i))

df = pd.DataFrame(dat)
df.columns = ['continent', 'longit', 'latit']
#df.to_csv
df.to_pickle("Country_Long_Lat.pkl")

output = pd.read_pickle("Country_Long_Lat.pkl")

print (output)


#GetCoordinates('Rocky Ford Colorado')
#GetCoordinates('Boulder Colorado')
#GetCoordinates('honolulu hi')
#GetCoordinates('honolulu')
#x= GetCoordinates('Boulder, Colorado')
#print(x[:-1])