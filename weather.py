# Modules
from assistant_details import aName
from speak import say
from requests import get
from bs4 import BeautifulSoup


def weather(place: str):
    """
    For weather forcast.
    :param place: str
    :return: Speak weather forcast of given place.
    """
    place = place.replace(aName, "")
    place = place.replace("temperature", "")
    place = place.replace("what is", "")
    place = place.replace("current", "")
    place = place.replace("tell me", "")
    place = place.replace("weather", "")
    place = place.replace(" the ", "")
    place = place.replace(" in ", "")
    place = place.replace("the", "")
    place = place.replace("in", "")
    place = place.strip()
    if place == "":
        return say("Sir! You didn't mentioned the place where you want to know the current weather.")
    else:
        try:

            say(txt="Searching.....")
            # creating url and requests instance
            url = "https://www.google.com/search?q=weather" + place
            html = get(url).content
            # getting raw data
            soup = BeautifulSoup(html, 'html.parser')
            temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
            str1 = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
            # formatting data
            data = str1.split('\n')
            time = data[0]
            sky = data[1]
            # getting all div tag
            listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
            strd = listdiv[5].text
            # getting other required data
            pos = strd.find('Wind')
            other_data = strd[pos:]
            if other_data == "?" or other_data == ".":
                return say(txt=f"Current Weather in {place} is {temp} and the sky is {sky}, at {time}.")
            else:
                return say(txt=f"Current Weather in {place} is {temp}, Sky is {sky} and other {other_data} at {time}.")
        except:
            say(txt=f"Sorry sir")
            return say(txt=" I couldn't fetch info due to the network issue or the place that you mentioned.")


if __name__ == '__main__':
    weather(place="Mumbai")
