# Modules
from requests import get
from json import loads
from speak import say
from listen import listen
from numpy import array, append

apiInd = "https://newsapi.org/v2/top-headlines?country=in&apiKey=cc1b8b053ad34203b6f9b87ee430ff42"  # indian Headlines
apiGlob = 'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=cc1b8b053ad34203b6f9b87ee430ff42'  # Global Headlines


def headlines(api: str):
    """For Headlines."""
    try:
        news = get(api).text
        news = loads(news)
        arts = news["articles"]
        head = array([])
        day = array(
            ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Last & Tenth"])
        for articles in arts:
            article = articles['title']
            head = append(head, array([article]))
        for i in range(len(day)):
            say(txt=f"Today's {day[i]} Headline is: {head[i]}.")
        return say(txt="That's all, Sir!")
    except:
        say(txt="I'm sorry sit! Due to the Network problem, I'm not able to fetch the latest headlines.")


def headlinesWhich():
    """To set API (India or Global) for the NEWS."""
    counter = 0
    reply = "who do you want to hear the headlines, About India or Global?"
    say(txt=reply)
    while True:
        which = listen().lower()
        if counter == 4 or counter == 9:
            say(txt=reply)
            counter += 1
        elif counter == 13:
            return say("The command has been canceled because you didn't respond.")
        elif which == 'none':
            counter += 1
        elif "exit" in which or "cancel the command" in which or "cancel command" in which or "cancel my command" in which or "go back" in which:
            return say("Okay sir!!!")
        elif "india" in which:
            return headlines(api=apiInd)
        elif "global" in which:
            return headlines(api=apiGlob)
        else:
            counter += 1


def latestNews():
    """For latest Headlines with categories."""
    counter = 0
    reply1 = "Which field news do you want to hear sir?"
    reply2 = "[Business], [Entertainment], [Health], [Science], [Sports], [Technology]."
    api_dict = {
        "Business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=cc1b8b053ad34203b6f9b87ee430ff42",
        "Entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=cc1b8b053ad34203b6f9b87ee430ff42",
        "Health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=cc1b8b053ad34203b6f9b87ee430ff42",
        "Science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=cc1b8b053ad34203b6f9b87ee430ff42",
        "Sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=cc1b8b053ad34203b6f9b87ee430ff42",
        "Technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=cc1b8b053ad34203b6f9b87ee430ff42"}
    url = None
    say(txt=reply1)
    say(txt=reply2)
    while True:
        try:
            query = listen().lower()
            if counter == 0 or counter == 4 or counter == 8:
                say(txt=reply1)
                say(txt=reply1)
                counter += 1
            elif counter == 13:
                return say("The command has been canceled because you didn't respond.")
            elif query == 'none':
                counter += 1
                pass
            elif "exit" in query or "cancel the command" in query or "cancel command" in query or "cancel my command" in query or "go back" in query:
                return say(txt="Okay sir.")
            else:
                for key, value in api_dict.items():
                    if key.lower() in query:
                        url = value
                        print(url)
                        say(txt="URL was found, Sir!")
                        break
                    else:
                        url = True
                if url is True:
                    say(txt="Sorry sir! URL was not found.")
                news = get(url).text
                news = loads(news)
                say(txt="Here is the first news.")
                arts = news["articles"]
                for articles in arts:
                    article = articles["title"]
                    say(article)
                    news_url = articles["url"]
                    print(news_url)
                    say(txt="For more information, Please visit website given above.")
                    say(txt="Do you want to know more about NEWS?")
                    query = listen().lower()
                    if "continue" in query or "yes" in query or "yah" in query or "yeah" in query or "of course" in query:
                        pass
                    else:
                        return say(txt="That's all, Sir!")
        except:
            say(txt="This category is not available in the present field!")
            say(txt="Please tell me category in the present field.")

