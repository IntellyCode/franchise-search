from urllib.request import urlopen,Request
import re
import pandas as ps
import googlesearch as gs
from bs4 import BeautifulSoup
import socket
import openpyxl as xl


def search(url,name,i):
    
    wb = xl.load_workbook("Output.xlsx")
    ws = wb.active
    print(url,i)
    req = Request(
    url, data=None, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
    )
    socket.setdefaulttimeout(10)
    f = urlopen(req).read().decode("utf-8")
    soup = BeautifulSoup(f,"html.parser").get_text()
    find = re.findall("franch",soup,re.IGNORECASE)
    
    if find !=[]:
        ws.append([name,'=HYPERLINK("{}")'.format(url)])
    wb.save("Output.xlsx")
        
    
file = ps.read_spss("company.sav")
i=1000

while i<10000:
    
    a = str(file._get_value(i,0,takeable=True))
    a=a.replace(", Inc.",'')
    a=a.replace(" Inc",'')
    i+=1
    try:
        for j in gs.search(a,num=3,start=0,stop=8,pause=0.5):
            try:
                search(j,a,i)
            except:
                continue
    except KeyboardInterrupt:
        print("skiped") 
        continue
    
    


