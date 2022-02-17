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
print('Bank code : '+ifsc[5:])
print("ifsc :"+ifsc)
#print("address : "+add)
print('Bank : '+branch[3:-2])
ac=d[1:2]
ac=str(ac)
ac=ac.split(",")
ac=ac[-1]
print('BRANCH :'+ac[1:-2])
print("address : "+add)
di=d[7:8]
di=str(di)
co=di.find("in \"")
lo=di.find("\" D")
print('District : '+di[co+4:lo])
st=d[5:6]
st=str(st)
print('state : '+st[2:-2])
