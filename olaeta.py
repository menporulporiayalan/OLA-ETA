import geocoder
from geopy.geocoders import Nominatim
from google import google

num_page = 1
search_results = google.search("Kalasipalayam bus stand latitude longitude", num_page)
for result in search_results:
 print(result.description)

geolocator = Nominatim(user_agent="specify_your_app_name_here")
city ="Bangalore"
country ="Ind"
loc = geolocator.geocode(city+','+ country)
print("latitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)

g = geocoder.ip('me')
print(g.latlng)

