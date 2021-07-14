from bs4 import BeautifulSoup
import requests
from pprint import pprint
import time

html = requests.get(
    'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=코로나')

soup = BeautifulSoup(html.text, 'html.parser')


data1 = soup.find('div', {'class': 'status_info'})

# 총 확진자 수와 오늘 확진자 수 찾기
total = data1.find('p', {'class': 'info_num'}).text
today = data1.find('em', {'class': 'info_variation'}).text


def corona():
    print("오늘의 코로나 확신자 소식 알려드릴게요.")
    print()
    time.sleep(2)
    print("오늘 발생한 코로나 확진자는 " + today + "명으로")
    time.sleep(1.5)
    print("총 확진 환자는 " + total + "명 입니다.")
    time.sleep(1.5)
    print("코로나 조심하세요!")


corona()
