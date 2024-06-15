# Modules
from database import getAnswerFromMemory
from speak import say
from random import choice
from battery_status import stopBatteryFile, systemPower
from attach_audio_file import playAudio
from os import system
import assistant_details
from assistant_modification import changeAssistantName, changeAVoice, dyChangeAName
from user_details import uName
from user_modification import changeUserName, dyChangeUName
from calendar_time import timeDateCombine, whatToday, todayDayName, todayHoliday, allHoliday
from location import myLocation, distance, distanceOnMap
from news import headlinesWhich, latestNews
from remember import setReminder, remember
from screenshot import takeSS
from system_info import realTimeCPUUse, totalRAM, availableRAM, usedRAM, usedRAMPercentage, memoryStatus, getOSName
from volume_controller import volumeUp, volumeDown, volumeMax, volumeMute
from app_open_close import openApp, closeApp
from search_internet import searchGoogle, searchWiki, searchYoutube
from weather import weather
from conversation import conversation


reply = ["Yes sir.", "Of course sir.", "Why not.", "Yes sir of course", "Of course sir why not.", "Yes sir why not."]


def process(query: str):
    """To process on the given queries. If queries available in the DataBase then it returns the value of the query."""
    answer = getAnswerFromMemory(question=query)
    if answer != "" and "can you" in query:
        say(txt=choice(reply))
    if "terminate yourself" in query or "turn the system offline" in query or "turn off system" in query or \
            "take the system offline" in query or "system offline" in query:
        reply1 = "I'm going to terminate myself", "I'm going to offline"
        if "terminate" in query:
            say(txt=f"Okay sir! I'm going to terminate myself.")
        elif "offline" in query:
            say(txt=f"Okay sir! I'm going to offline.")
        else:
            say(txt=f"Okay sir! {choice(reply1)}.")
        stopBatteryFile()
        playAudio(audioName="Sound\\Terminate_sound.wav")
        return exit()
    elif answer == "shutdown pc":
        say(txt=f"Okay sir.")
        say(txt="The system is going to shutdown.....")
        return system("shutdown /s /t 5")
    elif answer == "restart pc":
        say(txt=f"Okay sir.")
        say(txt="System restarting.....")
        return system("shutdown /r /t 5")
    elif answer == "sleep pc":
        say(txt=f"Okay sir.")
        say(txt="The system is going to sleep mode.....")
        return system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")
    elif answer == "get assistant name":
        return say(f"Sir my name is {assistant_details.aName}.")
    elif answer == "get assistant version":
        return say(txt=f"Sir my current version is {assistant_details.aVersion}.")
    elif answer == "change assistant name":
        return changeAssistantName()
    elif answer == "changeAVoice":
        return changeAVoice()
    elif answer == "get user name":
        return say(txt=f"Sir! Your name is {uName}.")
    elif answer == "change user name":
        return changeUserName()
    elif answer == "what today":
        return whatToday()
    elif answer == "day name":
        return todayDayName()
    elif answer == "get holiday":
        return todayHoliday()
    elif answer == "all holiday":
        return allHoliday()
    elif answer == "get power":
        return systemPower()
    elif answer == "get my location":
        return myLocation()
    elif answer == "get headline":
        return headlinesWhich()
    elif answer == "get news":
        return latestNews()
    elif answer == "get remember":
        return remember()
    elif answer == "get ss":
        return takeSS()
    elif answer == "cpu info":
        return realTimeCPUUse()
    elif answer == "total ram":
        return totalRAM()
    elif answer == "available ram":
        return availableRAM()
    elif answer == "ram use":
        return usedRAM()
    elif answer == "ram use per":
        return usedRAMPercentage()
    elif answer == "memory status":
        return memoryStatus()
    elif answer == "os name":
        return getOSName()
    elif answer == "volume max":
        return volumeMax()
    elif answer == "volume mute":
        return volumeMute()
# TODO: ****************************************************************************************************************
    elif answer == "dynamically can":
        return dyChangeAName(aNewAName=query)
    elif answer == "dynamically cun":
        return dyChangeUName(uNewName=query)
    elif answer == "open app":
        return openApp(appName=query)
    elif answer == "close app":
        return closeApp(appName=query)
    elif answer == "google search":
        return searchGoogle(query=query)
    elif answer == "wiki search":
        return searchWiki(query=query)
    elif answer == "yt search":
        return searchYoutube(query=query)
    elif answer == "get time":
        return timeDateCombine(query="get time")
    elif answer == "get date":
        return timeDateCombine(query="get date")
    elif answer == "get distance":
        return distance(place=query)
    elif answer == "get distance op":
        return distanceOnMap(place=query)
    elif answer == "remember":
        return setReminder(memory=query)
    elif answer == "volume up":
        return volumeUp(query=query)
    elif answer == "volume down":
        return volumeDown(query=query)
    elif answer == "get weather":
        return weather(place=query)
    else:
        return conversation(query=query)
