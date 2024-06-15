# Modules
from os import getpid
from database import updateValue
from psutil import sensors_battery
from threading import Thread
from speak import say
from subprocess import Popen
from win32gui import GetForegroundWindow, ShowWindow
from win32con import SW_HIDE

pid = str(getpid())
updateValue(table="memory_status", field="charging_pid", newValue=pid)


def isCharging():
    """For checks the charging is plugged in or plugged out."""
    while True:
        has_battery = sensors_battery().power_plugged
        if has_battery:
            while True:
                has_battery = sensors_battery().power_plugged
                if has_battery:
                    return say(txt="Charging is connected.")
        elif has_battery:
            while True:
                has_battery = sensors_battery().power_plugged
                if has_battery is False:
                    return say(txt="Charging is Disconnected.")


def plugged():
    """For execute isCharging() function in a loop."""
    while True:
        isCharging()


def batteryPowerAuto():
    """Battery status automation."""
    counter = 0
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    while True:
        has_battery = sensors_battery().power_plugged
        battery = sensors_battery()
        per = battery.percent
        if per == 100:
            counter = 0
        if per > 25:
            counter1 = 0
        if per > 15:
            counter2 = 0
        if per > 10:
            counter3 = 0
        if per > 50:
            counter4 = 0
        if has_battery is True and per == 99 and counter == 0:
            say(txt=f"Sir! my power is {per}%, Now you can disconnect the system from the charging point.")
            counter = 1
        if has_battery is True and per == 40 and counter4 == 0:
            say(txt=f"Sir! My power is {per}%, Now I'm ready for the work.")
            counter = 1
        if has_battery is False:
            if per == 25 and counter1 == 0:
                say(txt=f"Sir! My system have {per}% power, You should connect system to charging point to charge my system.")
                counter1 = 1
            elif per == 15 and counter2 == 0:
                say(txt=f"Sir! My system have {per}% power, I don't have enough power to work, Please connect to charging.")
                counter2 = 1
            elif per == 10 and counter3 == 0:
                say(txt=f"Sir! My system have {per}% power.")
                say(txt="My power is very low, Please connect to charging before the system shuts down.")
                counter3 = 1


def systemPower():
    """To battery percentage."""
    battery = sensors_battery()
    per = battery.percent
    say(f"Sir! My system have {per}% power.")
    if per > 40:
        return say("I have enough power to continue our work.")
    elif 15 < per <= 25:
        return say("You should connect the system to a charging point to charge the system.")
    elif 10 < per <= 15:
        return say("I don't have enough power to work, Please connect to charging.")
    elif 5 < per <= 10:
        return say("My power is very low, Please connect to charging before the system shuts down.")


def stopBatteryFile():
    """To stop automation file."""
    import database
    PID = database.getValue("memory_status", "charging_pid")
    return Popen(f'taskkill /f /PID {PID}', shell=True)


if __name__ == '__main__':
    hide = GetForegroundWindow()
    ShowWindow(hide, SW_HIDE)
    Thread(target=batteryPowerAuto).start()
    plugged()
    batteryPowerAuto()
