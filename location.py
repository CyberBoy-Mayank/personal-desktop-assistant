# Modules
from assistant_details import aName
from requests import get
from geocoder import ip
from webbrowser import open
from time import sleep
from speak import say
from geopy.geocoders import Nominatim
from geopy.distance import great_circle


def txtRemover(txt: str):
    """Extra text remover."""
    txt = txt.replace(aName, "")
    txt = txt.replace("current location", "")
    txt = txt.replace("present location", "")
    txt = txt.replace("what is the", "")
    txt = txt.replace("how far is", "")
    txt = txt.replace("where is", "")
    txt = txt.replace("location", "")
    txt = txt.replace("distance", "")
    txt = txt.replace("what is", "")
    txt = txt.replace("show me", "")
    txt = txt.replace("tell me", "")
    txt = txt.replace("present", "")
    txt = txt.replace("between", "")
    txt = txt.replace("from", "")
    txt = txt.replace("much", "")
    txt = txt.replace(" to ", "")
    txt = txt.replace("far", "")
    txt = txt.replace("the", "")
    txt = txt.replace("and", "")
    txt = txt.replace("our", "")
    txt = txt.replace("how", "")
    txt = txt.strip()
    return txt


def myLocation():
    """Find current location."""
    try:
        say(txt="Wait sir! I'm checking...")
        ip_add = get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
        geo_q = get(url)
        geo_d = geo_q.json()
        city = geo_d['city']
        state = geo_d['region']
        country = geo_d['country']
        latitude = geo_d['latitude']
        longitude = geo_d['longitude']
        say(f"Sir! We are in {city} city of {state} in {country}.")
        return say(txt=f"The Latitude is {latitude} and the Longitude is {longitude} of our current location.")
    except:
        return say(txt="Sorry sir! Due to the network issue I'm not able to find our current location.")


def distance(place: str):
    """Find distance."""
    placeName = txtRemover(txt=place)
    if placeName != "" or placeName != 'none':
        try:
            say(txt="Please wait sir! I'm checking...")
            geolocator = Nominatim(user_agent="myGeocoder")
            location = geolocator.geocode(placeName, addressdetails=True)
            target_latlong = location.latitude, location.longitude
            location = location.raw['address']
            target = {'city': location.get('city', ''), 'country': location.get('country', '')}
            current_loc = ip('me')
            current_latlong = current_loc.latlng
            distances = str(great_circle(current_latlong, target_latlong))
            distances = str(distances.split(' ', 1)[0])
            distances = round(float(distances), 2)
            say(str(target))
            return say(txt=f"Sir! The {placeName} is {distances} kilometres away from our current location.")
        except:
            return say(txt="Sorry sir! I couldn't find the place you mentioned.")
    else:
        return None


def distanceOnMap(place: str):
    """Find place on Google map."""
    placeName = txtRemover(txt=place)
    if placeName != "" or placeName != 'none':
        try:
            say(txt="Please wait sir! I'm checking...")
            url_place = 'https://www.google.com/maps/place/' + str(placeName)
            geolocator = Nominatim(user_agent="myGeocoder")
            location = geolocator.geocode(placeName, addressdetails=True)
            target_latlong = location.latitude, location.longitude
            location = location.raw['address']
            target = {'city': location.get('city', ''), 'country': location.get('country', '')}
            current_loc = ip('me')
            current_latlong = current_loc.latlng
            distances = str(great_circle(current_latlong, target_latlong))
            distances = str(distances.split(' ', 1)[0])
            distances = round(float(distances), 2)
            open(url=url_place)
            sleep(7)
            say(str(target))
            return say(txt=f"Sir {placeName} is {distances} kilometres away from our current location.")
        except:
            return say(txt="Sorry sir! I couldn't find the place you mentioned.")
    else:
        return None
