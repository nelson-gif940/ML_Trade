#testing

import numpy as np
from PIL import Image
import os
import sys
import shutil

#0. Useful fonctions

def splt(string):
    output = string.split("_")
    output_gif=output[4].split(".")
    output_gif=output_gif[0]+"."+output_gif[1]
    output=[float(output[1]),float(output[2]),float(output[3]),float(output_gif)] #low,high,open,close
    return output


#1. Get the data

os.chdir('C:/Users/nelso/Desktop/Classification_1/ressources')
arr=os.listdir() #starting price array

data=[]
id=[]
for i in range(len(arr)):
    data.append(splt(arr[i]))
    id.append(arr[i])

#2. Move each files to the new location

for i in range(len(data)-1):
    if(float(data[i+1][0])<float(data[i][0])):
        shutil.copyfile(id[i],'C:/Users/nelso/Desktop/Classification_1/Sorted/Loss/'+str(i)+".gif")
    if(float(data[i+1][0])>float(data[i][0])):
        if((float(data[i+1][3])-float(data[i+1][2]))/(float(data[i][3])-float(data[i][0]))<1 and (float(data[i+1][3])-float(data[i+1][2]))/(float(data[i][3])-float(data[i][0]))>0):
            shutil.copyfile(id[i],'C:/Users/nelso/Desktop/Classification_1/Sorted/Win_1/'+str(i)+".gif")
        if((float(data[i+1][3])-float(data[i+1][2]))/(float(data[i][3])-float(data[i][0]))<2 and (float(data[i+1][3])-float(data[i+1][2]))/(float(data[i][3])-float(data[i][0]))>1):
            shutil.copyfile(id[i],'C:/Users/nelso/Desktop/Classification_1/Sorted/Win_2/'+str(i)+".gif")
        if((float(data[i+1][3])-float(data[i+1][2]))/(float(data[i][3])-float(data[i][0]))<3 and (float(data[i+1][3])-float(data[i+1][2]))/(float(data[i][3])-float(data[i][0]))>2):
            shutil.copyfile(id[i],'C:/Users/nelso/Desktop/Classification_1/Sorted/Win_3/'+str(i)+".gif")
        if((float(data[i+1][3])-float(data[i+1][2]))/(float(data[i][3])-float(data[i][0]))<100 and (float(data[i+1][3])-float(data[i+1][2]))/(float(data[i][3])-float(data[i][0]))>3):
            shutil.copyfile(id[i],'C:/Users/nelso/Desktop/Classification_1/Sorted/Win_4/'+str(i)+".gif")
        print(i,(float(data[i+1][3])-float(data[i+1][2]))/(float(data[i][3])-float(data[i][0])))
