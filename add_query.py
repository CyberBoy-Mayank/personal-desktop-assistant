# Modules
from speak import say
from listen import listen
from database import getAnswerFromMemory, insertQuestionAndAnswer


def addQuery(query: str):
    """TODO: Value available in DataBase but query not available in DataBase, so it takes a queries dynamically from the user."""
    counter = 0
    dic = ["it means", "it mean", "its means", "its mean", "it's means", "it's mean"]
    say(txt=f"Can you please tell me what is the meaning of {query}.")
    while True:
        ans = listen().lower()
        if counter == 4 or counter == 9:
            say(txt="Can you please tell me what this mean?")
            counter += 1
        elif counter == 13:
            return say(txt="The command has been canceled because you didn't respond.")
        elif "exit" in ans or "cancel the command" in ans or "cancel my command" in ans or "cancel command" in ans or "go back" in ans:
            return say(txt="Okay sir!!!")
        elif ans == 'none' or ans == "" or ans is None:
            counter += 1
        elif "nothing" in ans or "so nothing" in query or "exit" in ans:
            return say(txt="Okay sir.")
        else:
            for i in dic:
                if i in ans:
                    ans = ans.replace(i, "")
                    ans = ans.strip()
                    try:
                        value = getAnswerFromMemory(question=ans)
                        if value == "":
                            return say(txt="Can't help with this one sir!")
                        else:
                            insertQuestionAndAnswer(question=query, answer=value)
                            return say(txt="Thanks! I'll remember it for the next time.")
                    except:
                        return say(txt="The DataBase is locked.")
                else:
                    counter = 4
