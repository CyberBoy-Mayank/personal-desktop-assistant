# Modules
from datetime import datetime
from speak import say
from listen import listen
from time import sleep
from pyautogui import screenshot
from assistant_details import aName


def dateTimeAutoName():
    """This function is used to generate name according to date and time."""
    strTime = datetime.now().strftime("%H-%M-%S")
    now = datetime.now()
    month_name = now.month
    day_name = now.day
    year_name = now.year
    mName = datetime.strptime(str(month_name), "%m")
    ordinalNames = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th',
                    '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th',
                    '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
    dn = ordinalNames[day_name - 1]
    mn = mName.strftime("%b")
    auto_name = f"{mn}-{dn}-{year_name}_{strTime}"
    return auto_name


def takeSS():
    """This function is used to take a screenshot."""
    counter1 = 0
    say(txt="Sir! Please tell me the name for this screenshot.")
    while True:
        name = listen().lower()
        name = name.replace(aName, "")
        name = name.strip()
        if counter1 == 4 or counter1 == 9:
            say(txt="Sir! Please tell me the name for this screenshot.")
            counter1 += 1
        elif name == 'none':
            counter1 += 1
        elif counter1 == 13:
            return say(txt="The command has been cancel because you didn't respond.")
        elif name == "exit" or "cancel my command" in name or "cancel command" in name or "go back" in name:
            return say(txt=f"Okay sir.")
        elif "give yourself" in name:
            if "give yourself" in name:
                say(txt="Okay sir!")
            say(txt="I name the screenshot according to the date & time.")
            try:
                sleep(2)
                img = screenshot()
                img.save(f"Screenshots\\{dateTimeAutoName()}.png")
                say(txt=f"I'm done sir! The screenshot is saved with the name {dateTimeAutoName()} in your main folder.")
            except:
                return say(txt="Something wants wrong.")
            return say(txt="Now I'm ready for the next command.")
        else:
            try:
                sleep(2)
                img = screenshot()
                name = name.strip()
                name = name.capitalize()
                img.save(f"Screenshots\\{name}.png")
                say(txt=f"I'm done sir! The screenshot is saved with the {name} in your main folder.")
            except:
                return say(txt="Something wants wrong.")
            return say(txt="Now I'm ready for the next command.")
