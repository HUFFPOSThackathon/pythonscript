import geocoder
from geopy.geocoders import Nominatim

#add the x y coordinates of the input 
g = geocoder.mapquest([28.627483,77.109601], method='reverse', key='nY4pFAlOkYIsn5ka8706grpCT1fv3Wtj')

# print g.json
zip = str(g.json['postal'])

geolocator = Nominatim()

location = geolocator.geocode(zip)

print location.address


