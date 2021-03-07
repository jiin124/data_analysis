from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

baseurl='https://www.google.com/search?q='
plusurl=input("무엇을 검색할까요:")
url=baseurl+quote_plus(plusurl)

driver=webdriver.Chrome()
driver.get(url)

html=driver.page_source
soup=BeautifulSoup(html)

r=soup.select('.yuRUbf')
for i in r:
    print(i.select_one('.LC20lb.DKV0Md').text)
    print(i.select_one('.TbwUpd.NJjxre').text)
    print(i.a.attrs['href'])
    print()

driver.close()
