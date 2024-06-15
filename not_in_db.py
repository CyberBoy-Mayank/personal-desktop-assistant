# Modules
from speak import say
from listen import listen
from search_internet import searchWiki
from add_query import addQuery


def notInDatabase(query: str):
    """Search on the internet or add query in database."""
    counter = 0
    say(txt="Sorry sir! It's not in my DataBase, Should I search on internet?")
    while True:
        ans = listen().lower()
        if counter == 4 or counter == 9:
            say(txt="Please tell me sir, Should I search on internet?")
            counter += 1
        elif counter == 13:
            return say(txt="The command has been canceled because you didn't respond.")
        elif ans == "none":
            counter += 1
        elif "cancel the command" in ans or "cancel my command" in ans or "cancel command" in ans:
            return say(txt="Okay sir!")
        elif "yes" in ans or "ok" in query or "okay" in query or "of course" in query or "why not" in query or "yeah" in query \
                or "yap" in query or "do it" in query:
            return searchWiki(query=query)
        elif "no" in ans or "do not" in query or "don't do it" in query or "do not do it" in query or "dont do it" in query \
                or "nope" in query:
            return addQuery(query=query)
        else:
            counter = 4
