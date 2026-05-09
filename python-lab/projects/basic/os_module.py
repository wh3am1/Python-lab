import os
import subprocess

path = "/home/allinone/Downloads"

content = (os.listdir(path))
print("================================================")
print("         Wellcome to Projects                   ")
print("================================================")
for i, item in  enumerate(content, start=1):
    print(i, content)
command = subprocess.run(["ls", "-lah"], capture_output=True, text=True)
print(command.stdout)