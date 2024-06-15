# Modules
from plyer import notification


def notif(title: str, msg: str, icon: str, timeout: int):
    """This function is used to display notification."""
    notification.notify(title=title, message=msg, app_icon=icon, timeout=timeout)
