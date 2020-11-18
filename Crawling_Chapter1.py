
from urllib.request import urlopen
html = urlopen('http://pythonscraping.com/pages/page1.html')
print(html.read())

# 1.2 BeautifulSoup 소개
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page1.html")

#---------------------------------------------
# BeautifulSoup(html텍스트, 구문 분석기)
bs = BeautifulSoup(html.read(), 'html.parser')

print(bs.h1)
print(bs.html.body.h1)
print(bs.body.h1)
print(bs.html.h1)

#---------------------------------------------
import lxml # 형식 지키지 않은 지저분한 html 분석
bs=  BeautifulSoup(html.read(), 'lxml')

#---------------------------------------------
# 에러 [HTTPError]
# 1. 페이지를 찾을 수 없거나, URL 해석에서 에러가 생긴 경우
# 2. 서버를 찾을 수 없는 경우
# 3. 존재하지 않는 태그에 접근 시도하면 None 객체 반환

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html  = urlopen(url)
    except HTTPError as e :
        return None

    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title==None:
    print("Title could not be found")
else:
    print(title)