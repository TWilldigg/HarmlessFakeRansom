import os

desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') #Find desktop of logged on user
desktop = desktop + "\encrypted" ##Test path or create it

if not os.path.exists(desktop):
    os.makedirs(desktop)

text = "Tool Created by TWildigg & Jkerai1" # Input the names here for the encrypted files
FileList = text.split(' ') 

for i in FileList:
    index = str(FileList.index(i)) + ") " + i
    FileList[FileList.index(i)] = index #Rewrite Element in List with Numbered Text to Maintain order of string

for file in FileList:
    temp = desktop + "\\" + file + ".encrypted" # Build final path
    f = open(temp,"w")
    f.close()

path = os.path.realpath(desktop)
os.startfile(path) #Open to the Folder holding the encrypted files
