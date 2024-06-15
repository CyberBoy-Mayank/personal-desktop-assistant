# Modules
from psutil import cpu_percent, virtual_memory
from speak import say

t_ram = round(virtual_memory().total / 1000000000, 2)
a_ram = round(virtual_memory().available / 1000000000, 2)
u_ram = round(virtual_memory().used / 1000000000, 2)
u_ram_p = virtual_memory().percent


def realTimeCPUUse():
    """This function is used to know real time cup usage."""
    from assistant_details import aName
    say(txt="CPU Usage", prnt=False)
    for _ in range(2):
        cpu = (cpu_percent(interval=1))
        print(f"\r{aName}: CPU use:- {cpu}%", end="")
        say(txt=f"{cpu}%", prnt=False)
    print()


def totalRAM():
    """
    This function is used to know the total RAM.
    :return: t_ram: float.
    """
    return say(txt=f"{t_ram}GB total RAM in my system.")


def availableRAM():
    """
    This function is used to know available RAM.
    :return: a_ram: float.
    """
    return say(txt=f"{a_ram}GB RAM remaining in my system.")


def usedRAM():
    """
    This function is used to know currently uses RAM in GB.
    :return: u_ram: float
    """
    return say(txt=f"My system currently uses {u_ram}GB of RAM.")


def usedRAMPercentage():
    """
    This function is used to know currently uses of RAM in percentage.
    :return: u_ram_p: float
    """
    return say(txt=f"My system currently uses {u_ram_p}% of RAM.")


def memoryStatus():
    """This function is used to combine some functions that consist of information about RAM."""
    say(txt=f"My system has a total {t_ram}GB RAM.")
    say(txt=f"{a_ram}GB RAM remaining, In percentage {100 - u_ram_p:.2f}% RAM remaining in my system.")
    return say(txt=f"{u_ram}GB RAM used, In percentage {u_ram_p}% RAM used in my system.")


def getOSName():
    """This function is used to retrieve the operating system name."""
    from platform import system
    return system()


def isOS(os_name):
    """
    :param os_name: str.
    :return: boolean
    """
    if getOSName() == os_name:
        return True
    else:
        return False
