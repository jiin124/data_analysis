import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/list.nhn?titleId=654774&weekday=mon"
res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")

cartoons=soup.find_all("td",attrs={"class":"title"})
rate=soup.find_all("div",attrs={"class":"rating_type"})

#title=cartoons[0].a.get_text()
#link=cartoons[0].a["href"]
#print(title)
#print("https://comic.naver.com"+link)

for i in range(len(cartoons)):
    title=cartoons[i].a.get_text()
    link="https://comic.naver.com"+cartoons[i].a["href"]
    rates=rate[i].strong.get_text()
    print(title)
    print(link)
    print(rates)
    print()



#for cartoon in cartoons:
 #   title=cartoon.a.get_text()
  #  link="https://comic.naver.com"+cartoon.a["href"]
   # print(title)
   # print(link)
   # print()