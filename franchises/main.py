import pandas as pd
import re
import word as w
import googlesearch as s

file = pd.read_spss('company.sav')
for index,row in file.iterrows():
    a = str(file._get_value(index,0,takeable=True))
    a=a.replace(", Inc.",'')
    a=a.replace(" Inc",'')
    name="output/"+a+".txt"
    output = open(name,"w")
    for j in s.search(a,lang='en',num=10,start=0,stop=10,pause=1.0):
        output.write(j+"\n")
    output.close()

