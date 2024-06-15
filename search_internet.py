# Modules
from pywhatkit import search, playonyt
from speak import say
from wikipedia import summary
from assistant_details import aName
from time import sleep


def textRemover(query: str):
    """
    This function is used to remove extra text from the user's query."""
    query = query.replace(aName, "")
    query = query.replace("search on the wikipedia", "")
    query = query.replace("search in the wikipedia", "")
    query = query.replace("search on the internet", "")
    query = query.replace("search in the internet", "")
    query = query.replace("search on wikipedia", "")
    query = query.replace("search in wikipedia", "")
    query = query.replace("search on internet", "")
    query = query.replace("search in internet", "")
    query = query.replace("search wikipedia", "")
    query = query.replace("on the wikipedia", "")
    query = query.replace("in the wikipedia", "")
    query = query.replace("search internet", "")
    query = query.replace("search youtube", "")
    query = query.replace("youtube search", "")
    query = query.replace("on the youtube", "")
    query = query.replace("search browser", "")
    query = query.replace("in the browser", "")
    query = query.replace("on the browser", "")
    query = query.replace("in the youtube", "")
    query = query.replace("browser search", "")
    query = query.replace("google search", "")
    query = query.replace("search google", "")
    query = query.replace("in the google", "")
    query = query.replace("on the google", "")
    query = query.replace("in the chrome", "")
    query = query.replace("on the chrome", "")
    query = query.replace("search in the", "")
    query = query.replace("search on the", "")
    query = query.replace("on wikipedia", "")
    query = query.replace("in wikipedia", "")
    query = query.replace("in youtube", "")
    query = query.replace("on youtube", "")
    query = query.replace("on browser", "")
    query = query.replace("in browser", "")
    query = query.replace("in google", "")
    query = query.replace("on google", "")
    query = query.replace("in chrome", "")
    query = query.replace("on chrome", "")
    query = query.replace("wikipedia", "")
    query = query.replace("wikipedia", "")
    query = query.replace("youtube", "j")
    query = query.replace("internet", "")
    query = query.replace("what is", "")
    query = query.replace("browser", "")
    query = query.replace("tell me", "")
    query = query.replace("search", "")
    query = query.replace("who is", "")
    query = query.replace("google", "")
    query = query.replace("chrome", "")
    query = query.replace("search", "")
    query = query.replace("about", "")
    query = query.strip()
    return query


def searchGoogle(query: str):
    """Search on the Google."""
    try:
        say(txt="Searching in the Google.....")
        query = textRemover(query=query)
        search(query)
        result = summary(title=query, sentences=2)
        sleep(7)
        say(txt=f"Sir! This is what I found for your search on the Google....\n{result}")
        return say(txt="That's all sir.")
    except:
        return say(txt=f"Sorry sir! No speakable output available.")


def searchWiki(query: str):
    """Search on wikipedia."""
    try:
        query = textRemover(query=query)
        results = summary(title=f'{query}', sentences=2)
        say(txt=f"According to wikipedia.....\n{results}")
        return say(txt="That's all sir.")
    except:
        return say(txt=f"Sorry sir! No speakable output available.")


def searchYoutube(query: str):
    """Search on the YouTube."""
    try:
        query = textRemover(query=query)
        playonyt(query)
    except:
        return say(txt="Something wants wrong.")
