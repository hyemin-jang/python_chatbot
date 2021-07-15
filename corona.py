from bs4 import BeautifulSoup
import requests
import time

html = requests.get(
    'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=코로나')

soup = BeautifulSoup(html.text, 'html.parser')

# 총 확진자 수와 오늘 확진자 수 찾기
# select()
total = soup.select('p.info_num')[0].get_text()
today = soup.select('em.info_variation')[0].get_text()
# find()
#total = soup.find('p', {'class': 'info_num'}).text
#today = soup.find('em', {'class': 'info_variation'}).text


def corona():
    print("오늘 코로나 확진자 현황 알려드릴게요.")
    print()
    time.sleep(2)
    print("오늘 발생한 코로나 확진자는 " + today + "명으로")
    time.sleep(1.5)
    print("총 확진 환자는 " + total + "명 입니다.")
    time.sleep(1.5)
    print("코로나 조심하세요!")


corona()
