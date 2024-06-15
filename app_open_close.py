# Modules
from time import sleep
from assistant_details import aName
from speak import say
from pyautogui import press, typewrite
from keyboard import press_and_release
from os import system

dictApp = {"command-prompt": "cmd", "commandprompt": "cmd", "command prompt": "cmd", "cmd": "cmd", "paint": "paint",
           "word": "winword", "excel": "excel", "chrome": "chrome", "vscode": "code", "powerpoint": "powerpnt",
           "camera": 'WindowsCamera',
           'microsoftedge': 'msedge', 'microsoft edge': 'msedge', 'pycharm': 'pycharm64', 'this pc': 'explorer',
           'file manager': 'explorer',
           'file explorer': 'explorer', 'this computer': 'explorer', 'virtual box': 'VirtualBox',
           'oracle virtual box': 'VirtualBox', 'db browser': 'sqlite3', 'sqlite': 'sqlite3', 'firefox': 'firefox',
           'fire fox': 'firefox', 'picasa': 'Picasa3', 'vlc media player': 'Vlc', 'media player': 'Vlc',
           'pc remote receiver': 'PCRemoteReceiver', 'remote receiver': 'PCRemoteReceiver',
           'music player': 'mswindowsmusic',
           'groove': 'mswindowsmusic'}


def openApp(appName: str):
    """This function is used to open the applications."""
    appName = appName.replace("website", "")
    appName = appName.replace("web site", "")
    appName = appName.replace("launch", "")
    appName = appName.replace("open", "")
    appName = appName.replace("app", "")
    appName = appName.replace("application", "")
    appName = appName.replace("the", "")
    appName = appName.replace(aName, "")
    appName = appName.strip()
    if appName == '':
        return
    else:
        try:
            press("super")
            typewrite(appName)
            sleep(1)
            press("enter")
        except:
            say(txt="Something wants wrong.")


def closeApp(appName: str):
    """This function is used to close the applications."""
    appName = appName.replace("exit", "")
    appName = appName.replace("close", "")
    appName = appName.replace("the", "")
    appName = appName.replace(aName, "")
    appName = appName.strip()
    if appName == '' or appName is None:
        return
    elif "the current window" in appName or "window" in appName or "the window" in appName or "current window" in appName:
        return press_and_release('alt + f4')
    else:
        for app in list(dictApp.keys()):
            if app in appName:
                try:
                    return system(f"taskkill /f /im {dictApp[app]}.exe")
                except:
                    return say(txt="Somthing wants wrong.")


if __name__ == '__main__':
    openApp("cmd")
    sleep(5)
    closeApp("cmd")
