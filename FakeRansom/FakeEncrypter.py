import os
import time

desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') #Find desktop of logged on user
desktop = desktop + "\encrypted" ##Test path or create it

if not os.path.exists(desktop):
    os.makedirs(desktop)

text = "RIP BOZO PACKWATCH" # Input the names here for the encrypted files
FileArray = text.split(' ') ##Split to array

for i in FileArray:
    index = str(FileArray.index(i)) + ") " + i
    FileArray[FileArray.index(i)] = index

for file in FileArray:
    temp = desktop + "\\" + file + ".encrypted" # Build final path
    f = open(temp,"w")
    f.close()

path = os.path.realpath(desktop)
os.startfile(path)
