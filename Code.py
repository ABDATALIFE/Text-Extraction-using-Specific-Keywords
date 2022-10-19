#%%
import pandas as pd


#%%
idlist = []
nameslist = []
moneylist = []

#%%
with open('Trial.txt','r') as f:
    s = f.readlines()
    for x in s:
        if x.__contains__("EPD"):
            start = x.find("EPD") + len("EPD")
            end = x.find("VCAD")
            substring = x[start:end] + " - "
            substring2=substring.strip(" ")
            substring3 = substring2.split(" ")
            idlist.append(substring3[0])
            nameslist.append(substring3[1:5])
        if x.__contains__("Money"):
            start = x.find("EPD") + len("EPD")
            end = x.find("VCAD")
            substring = x[start:end] + " - "
            substring2=substring.strip(" ")
            substring3 = substring2.split(" ")
            idlist.append(substring3[0])
            nameslist.append(substring3[1:5])
        
            

                    
            
    f.close()
    
    

