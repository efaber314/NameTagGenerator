#This code can be modified to take in a list of names and affiliations and
#print them onto an image file that must be saved in the same directory.
#Emily Faber
#Made for the 2020 Earth Day symposium at UMBC

from PIL import Image, ImageDraw, ImageFont
import pandas as pd

#df = pd.read_csv('Response.csv')
#myList = df['Name']
#myAffiliations = df['Affiliations']

#EITHER import from a csv (Above) or create a list (below)

#myList = []
#myAffiliations = []
n = 0 # number of name tags that are left to print on a sheet


sheets = 1 #start with sheet 1
x = 75 #initial placement of text
y = 120 #initial placement of text
flag = 0 #used to switch rows
flag2 = 0 #used to switch to 3rd row

with Image.open('BlankNameTags.png') as image:
    for i in range(len(myList)):

        #this if changes to a new sheet when triped
        if n > 5: #change 5 for different number of total nametags on sheet
            image.save('Nametag'+str(sheets)+'.png')
            image.close()
            image =Image.open('BlankNameTags.png') #opens new blank sheet
            sheets += 1
            #resets number of names and locations
            n = 0
            x = 75
            y = 120

        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('arial.ttf', 28, encoding = "unic")

        #creates new nametag text
        myString = myList[i] + "\n" + myAffiliations[i]
        draw.text((x,y), myString,font=font, fill = (0,0,0))
        n += 1
        flag += 1

        #changes row and collumn values to print at
        if flag > 1:
            flag = 0
            x = 75
            y = 420
            flag2 += 1
            if flag2 > 1:
                flag2 = 0
                x = 75
                y = 740
        else:
            x += 400

    #saves final sheet even if it isn't full
    image.save('Nametag'+str(sheets)+'.png')
    image.close()
