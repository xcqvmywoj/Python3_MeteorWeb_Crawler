#coding=utf-8
import requests
from bs4 import BeautifulSoup
import lxml
#送出GET請求到遠端伺服器，伺服器接受請求後回傳<Response [200]>，代表請求成功
res = requests.get("https://meteor.today/article/share/589d8823ef79368d7d69bc0f")
#經過BeautifulSoup內lxml編輯器解析的結果
soup = BeautifulSoup(res.text,'lxml')
#留言樓層
floor = (soup.select('h6')[3].text)
floorname = floor.strip().split(' ')
floorcontent = (soup.select('p')[3].text)
floorsup = floorcontent.strip().split('/')
values = {floorname[1]: floorsup[0]}

MessageNumber = soup.select('button')[6].text
MessageNumberFloor = int(MessageNumber)*2
j = 1
for i in range(1,MessageNumberFloor):
    if(i%2)!=0:
        #print (soup.select('h6')[i].text)
        floor = (soup.select('h6')[i].text)
        floorname = floor.strip().split(' ')
        j+=1
        #print (soup.select('p')[j].text)
        floorcontent = (soup.select('p')[j].text)
        floorsup = floorcontent.strip().split('/')
        values[floorname[1]] = floorsup[0]
SupN = 0
nSupN = 0
unknown = 0
for value in values.values():
    #print(value)
    if(value.startswith("支持")):
        SupN+=1
    elif(value.startswith("反對")):nSupN+=1
    else:unknown+=1
print("支持人數：",SupN,"人，","反對人數：",nSupN,"人，","格式不明：",unknown,"人。")