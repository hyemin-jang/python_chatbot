from os import name
import requests
from bs4 import BeautifulSoup
import time

search_word = None
def todayNews():

    titles = []

    global search_word
    search_word = input("보고 싶은 뉴스 키워드를 입력하세요\n")
    url = f'https://m.search.naver.com/search.naver?where=m_news&sm=mtb_jum&query={search_word}'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    search_result = soup.select_one('#news_result_list')
    news_links = search_result.select('.bx > .news_wrap > a')

    for title in news_links:
        titles.append(title.get_text())

    time.sleep(1)
    print(search_word, "최신 뉴스 5개를 알려드립니다.")
    print()

    for i in range(5):
        print("-", titles[i])

#     뉴스 링크 추가하기
#     print(nkeyword)
