import sys
print("$$ Modules Builtin -\n",sys.builtin_module_names)
print("$$ Path - ",sys.prefix)
import time
import os

while True:
    if(os.path.exists("test.txt")):
        with open("test.txt") as myFile:
            print(myFile.read())
            time.sleep(3) # in seconds
    else:
        print("File Not Found")


# Install pandas - pip install pandas