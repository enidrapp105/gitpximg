import os
import datetime
from PIL import Image

def editfile(edit, numfiles, cdate, adate):
    for x in range(numfiles):
        with open("file" + str(x) + ".txt", 'w') as file:
            file.write(str(edit))
        
        os.system(authordate + committerdate + "git add file" + str(x) +".txt; git commit -m \"commit from "+ str(edit) +"\"")

img = Image.open('dragon.png')
count = 0
pixels = img.load()
date = datetime.datetime(2017, 1, 1)
width, height = img.size

for x in range(width):
    for y in range(height):
        authordate = "export GIT_AUTHOR_DATE=\"2017-" + date.strftime("%m") + "-" + date.strftime("%d") + "T12:00:00\"; "
        committerdate = "export GIT_COMMITER_DATE=\"2017-" + date.strftime("%m") + "-" + date.strftime("%d") + "T12:00:00\"; "
        print(authordate)
        print(committerdate)
        r, _, _, _ = pixels[x, y]
        #white
        if r == 255:
            #print("white ", count)
            editfile(date, 3, committerdate, authordate);
        #black
        if r == 0:
            #print:("black", count)
            editfile(date, 0, committerdate, authordate);
        #dark gray
        if r == 139:
            #print("dark gray", count)
            editfile(date, 1, committerdate, authordate);
        #light gray
        if r == 195:
            #print("light gray", count)
            editfile(date, 2, committerdate, authordate);
        count = count + 1
        date += datetime.timedelta(days=1)

