import pandas as pd
import googlesearch as s
import word as w
file = pd.read_spss('company.sav')
output = open("links.txt","a")
def search(x):
    inp = open(name,'r')
    for line in inp:
        print(line)
        if w.word(line,"franch")!=0:
            output.write(a+" "+line +" " + w.word(line,"franch"))
    inp.close()    
for index,row in file.iterrows():
    a = str(file._get_value(index,0,takeable=True))
    a=a.replace(", Inc.",'')
    a=a.replace(" Inc",'')
    name="output/"+a+".txt"
    search(a)
output.close()
