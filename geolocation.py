#changing python env to anaconda: https://medium.com/@udiyosovzon/how-to-activate-conda-environment-in-vs-code-ce599497f20d

from geopy.geocoders import Nominatim

def GetCoordinates(EnterLocation):
    """returns coordinates [lat,long,address] when provided a geograhpic location as a string.
    
    Parameters: input type string. 
    
    Returns: tpye list with longitude and latitude,i.e., [long,lat]
        
    Note:This function is for finding geolocations for open layers map

    """
    # calling the Nominatim tool
    loc = Nominatim(user_agent="GetLoc")
    
    # entering the location name
    getLoc = loc.geocode(EnterLocation)
    
    # return found address
    #print(getLoc.address, '\n')

    return [getLoc.longitude,getLoc.latitude,getLoc]

#GetCoordinates('Rocky Ford Colorado')
#GetCoordinates('Boulder Colorado')
#GetCoordinates('honolulu hi')
#GetCoordinates('honolulu')
#x= GetCoordinates('Boulder, Colorado')
#print(x[:-1])