# Modules
from datetime import date, datetime
from random import choice
from assistant_details import aName, aVersion
from database import getValue, updateValue
from speak import say
from user_details import uName


# Wish Function.
def wishMe():
    """Wish (good morning, good afternoon, good evening or welcome back) according to the time when program run.
    return:
        NoneType: Greetings.
    """
    strH = datetime.now().strftime("%H:%M")
    say(f"It's {strH} O'clock.")

    # Fetch previous date
    previous_date = getValue("memory_status", "last_seen_date")
    # Fetch today's date and store it to DataBase
    today_date = str(date.today())
    updateValue("memory_status", "last_seen_date", today_date)
    hour = int(datetime.now().hour)

    if today_date == previous_date:
        # say(txt=f"Welcome Back {uName} sir.")
        say(txt=f"Welcome Back sir.")
    else:
        if 3 <= hour < 12:
            ans = f"Good Morning {uName} sir!", f"Hello {uName} sir! Good Morning..."
            say(txt=choice(ans))
        elif 12 <= hour < 16:
            ans = f"Good Afternoon {uName} sir!", f"Hello {uName} sir! Good Afternoon..."
            say(txt=choice(ans))
        else:
            ans = f"Good Evening {uName} sir!", f"Hello {uName} sir! Good Evening..."
            say(txt=choice(ans))
    say(txt=f"I'm Your Personal Assistant {aName} {aVersion}.")
    return say(txt="Please tell me, How can I help you sir?")


if __name__ == '__main__':
    wishMe()
