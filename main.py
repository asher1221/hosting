
import streamlit as st

from PIL import Image
import json

import sys

sys.path.append('/usr/lib/python3/dist-packages')
def forsets():
    lorlist=[]
    for i in range(1,5):
        one = "/Users/asherhounsell/Documents/LORDevelopment/set1-lite-en_us/en_us/data/set1-en_us.json"
        two = "/Users/asherhounsell/Documents/LORDevelopment/set2-lite-en_us/en_us/data/set2-en_us.json"

        string = "/Users/asherhounsell/Documents/LORDevelopment/set"+str(i)+"-lite-en_us/en_us/data/set"+str(i)+"-en_us.json"
        f = open(string)
        data = json.load(f)
        for a in range(len(data)):
            lorlist.append(data[a])
    #print(lorlist)
    leng = len(lorlist)
    #print(leng)
    newlorlist=[]
    for i in range(len(lorlist)):
        newdict ={}
        #print(lorlist[i]["name"])
        for a in lorlist[i]:
            #print(a)
            #print(lorlist[i][a])
            if a!="assets":
                if isinstance(lorlist[i][a], list):
                    if not lorlist[i][a]:
                        add = ""
                    else:
                        add=lorlist[i][a][0]
                else:
                    add=lorlist[i][a]
                newdict[a]=add
        newlorlist.append(newdict)

    # df = pd.DataFrame.from_dict(newlorlist)
    # #print (df)
    # df.to_excel("/Users/asherhounsell/Documents/LORDevelopment/dict1.xlsx")
    #print(newlorlist)
    # for i in range(len(newlorlist)):
    #     if newlorlist[i]["rarityRef"] == "Champion":
    #         newlorlist[i+1]["name"]=newlorlist[i+1]["name"]+"2"
    return newlorlist

# def lookup(lookingfor,incat,outcat):
#     for i in data:
#         try:
#             if i[incat] == lookingfor:
#                 return i[outcat]
#         except TypeError:
#             print("Not a card.\n")
# def inputer():
#     go = input("Do you want to look up a card? (y/n) ")
#     while go == "y" or go == "Y":
#         val = input("Lookup Card: ")
#         try:
#             code = lookup(str(val),"name","cardCode")
#             filename = "/Users/asherhounsell/Documents/LORDevelopment/pics/" + code + ".png"
#             image = Image.open(filename)
#             image.show()
#         except TypeError:
#             print('Not a card')


    return

data = forsets()


#


st.write("""
# Ashers Web App
Some Testing Below

Hello
""")

filename = "/Users/asherhounsell/Documents/LORDevelopment/pics/" + data[43]["cardCode"] + ".png"
image = Image.open(filename)
st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

