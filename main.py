import subprocess
import platform

subprocess.run(["py","-m", "pip", "install","pipenv"])
subprocess.run(["py","-m", "pipenv", "install"])
import os

if platform.system() == "Windows":
    os.system('cls')  # For Windows
else:
    os.system('clear')  # For Linux/OS X

from Folder1 import script
from lib import util

import sys
print("---------------------------")
print(sys.executable)
print('_________________________')

# subprocess.run(["py","-m","Folder1.script"])
script.main()
print("done")