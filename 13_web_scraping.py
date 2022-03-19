'''
웹 스크래핑 절차
1) 원하는 페이지에 request를 보내서, 결과 html을 받는다
2) 받은 htim을 파싱한다
3) 필요한 정보만 추출한다.
'''


'''
네이버 영화 랭킹 읽어오기
 - html 구조:
   <태그명 속성명1="속성값1" 속성명2="속성값2"> 텍스트 </태그명>
'''


# find, find_all('태그명', {'속성명':'값'...})
soup.find('title')   # 해당 조건에 맞는 하나의 태그만 반환(여러개의 경우 첫번째만)
soup.find_all('h1')  # 해당 조건에 맞는 태그 모두 반환
soup.find_all('a', {'id': 'link2', 'link3'})    # 속성 id가 link2 또는 link3의 값을 가진 a 태그 모두 반환
soup.find_all('a', {'class':'sister', {'id': 'link2', 'link3'}})    # 속성 class가 sister이면서 동시에 속성id가 link2 또는 link3의 값을 가진 a 태그 모두 반환
get_text()           # 태그와 태그사이의 값 반환     


# 속성에 접근
<a href="http://example.com/elsie" class="syster" id="link1">Elsie</a>
alist = soup.find_all('a')
for atag in alist:
  print(atag.get('href'))


# 네이버 영화 랭킹 웹스크래핑
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = https://movie.naver.com/movie/sdb/rank/rmovie.naver  # 웹페이지

page = urlopen(url)  # 웹페이지 읽어오기
soup = BeautifulSoup(page, "html.parser")   # page 내용을 html로 해석

result = soup.find_all("div", {"class":"tit3"}

i = 1
for move in result:
   print("%2d위" %i, end='')
   print(movie.get_text().strip())
   i += 1
