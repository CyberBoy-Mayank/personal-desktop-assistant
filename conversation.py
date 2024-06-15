# Modules
from speak import say
from random import choice
from not_in_db import notInDatabase


def conversation(query: str):
    """Conversation with assistant."""
    if "hi" in query or "hey" in query or "hello" in query:
        ans = ["Hi sir! How are?", "Hello sir! How are?", "Hey sir! How are?", "Hi sir! How do you do?",
               "Hello sir! How do you do?", "Hey sir! How do you do?", "Hi sir! What's up?", "Hello sir! What's up?",
               "Hey sir! What's up?"]
        return say(txt=choice(ans))
    elif "I'm fine" in query or "i am fine" in query or "i'm perfect" in query or "i am perfect" in query \
            or "perfect" in query or "everything is good" in query or "everything is fine" in query \
            or "everything is perfect" in query or "everything good" in query or "everything fine" in query \
            or "everything perfect" in query or "i am ok" in query or "i am okay" in query or "i'm ok" in query \
            or "i'm okay" in query:
        ans = ["Oh!!! That's great sir!", "That's nice sir!"]
        return say(txt=choice(ans))
    elif "how are you" in query or "how do you do" in query or "what's up" in query:
        ans = ["I'm fine sir.", "I'm okay sir.", "perfect sir", "I'm good sir.", "Everything is fine sir.",
               "Everything is okay sir.", "Everything is okay sir.", "Everything is perfect sir.",
               "Everything is good sir."]
        return say(txt=choice(ans))
    elif "thank you" in query or "thanks" in query:
        ans = ["It's my pleasure sir!", "You're welcome", "My goodness sir!", "It wasn't a big deal sir!"]
        return say(txt=choice(ans))
    elif "what are you doing" in query:
        return say(txt="I'm waiting for your command.")
    elif "can i tell you something" in query:
        ans = 'Yes sir, Please tell me.'
        return say(txt=ans)
    else:
        notInDatabase(query=query)
