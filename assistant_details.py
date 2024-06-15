# Modules
from database import getValue

# Assistant's Name.
aName = getValue("memory_status", "assistant_name")

# Assistant's Version.
aVersion = getValue("memory_status", "assistant_version")

# Assistant's Voice.
aVoice = int(getValue("memory_status", "assistant_voice"))

if __name__ == '__main__':
    print(aName)
    print(aVersion)
    print(aVoice)
