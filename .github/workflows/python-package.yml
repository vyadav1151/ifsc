from bs4 import BeautifulSoup
import requests as re
import json
result=re.get('https://ifsc.bankifsccode.com/PUNB0394700')
hc=result.content
soup=BeautifulSoup(hc,"html.parser")
f=soup.find_all(text=True)
a=list(f)
b=a[120:160]

def Convert_dict(a):  
    init = iter(a)  
    res_dct = dict(zip(init, init))  
    return res_dct  
c=Convert_dict(b)
c
add=c['Address:']
#print(add)
ifsc=list(c.keys())
d=list(c.keys())
mm=d[1:2]
mn=str(mm)
mn=mn.split(",")
mb=mn[1:2]
mb=str(mb)
branch=mb
ifsc=ifsc[1:]
ifsc=ifsc[0:1]
ifsc=str(ifsc)
ifsc=ifsc[14:25]
print(ifsc[5:])
print(ifsc)
print("address :"+add)
print(branch[3:-2])
