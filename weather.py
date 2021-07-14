from bs4 import BeautifulSoup
import requests
from pprint import pprint
import time

html = requests.get('https://search.naver.com/search.naver?query=날씨')

soup = BeautifulSoup(html.text, 'html.parser')

data1 = soup.find('div', {'class': 'weather_box'})

# 현재 위치, 기온 찾기
location = data1.find('span', {'class': 'btn_select'}).text
temperature = data1.find('span', {'class': 'todaytemp'}).text

# 강수 확률
data2 = data1.find('li', {'class': 'date_info today'}
                   ).findAll('span', {'class': 'rain_rate'})
rain_rate1 = data2[0].find('span', {'class': 'num'}).text
rain_rate2 = data2[1].find('span', {'class': 'num'}).text


data3 = data1.find('div', {'class': 'detail_box'}).findAll('dd')

# 미세먼지
if (data3[0]):
    f_data = data3[0].get_text()
    idf = f_data.find('㎥')
    fine_dust = f_data[:idf+1]
    f_state = f_data[idf+1:]
    exc1 = 0
else:
    exc1 = 1

# 초미세먼지
if(data3[1]):
    fu_data = data3[1].get_text()
    idf = fu_data.find('㎥')
    fine_ultra_dust = fu_data[:idf+1]
    fu_state = fu_data[idf+1:]
    exc2 = 0
else:
    exc2 = 1

# 오존
if(data3[2]):
    o_data = data3[2].get_text()
    idf = o_data.find('m')
    ozone = o_data[:idf+1]
    o_state = o_data[idf+1:]
    exc3 = 0
else:
    exc3 = 1


def weather():
    print("지금 계신 " + location + "의 날씨를 알려드릴게요. 잠시만 기다려주세요")
    print()
    time.sleep(2)
    print("현재 " + location + "의 기온은 " + temperature + "℃ 입니다.")
    time.sleep(1)
    print("오전 강수 확률은 " + rain_rate1 + "%이고, 오후 강수 확률은 " + rain_rate2 + "%입니다.")
    time.sleep(1)
    rain(rain_rate1, rain_rate2)
    time.sleep(1)

    if exc1 + exc2 + exc3 == 0:
        print("미세먼지 농도는 " + fine_dust + "로 " + f_state + " 상태이고,")
        time.sleep(1)
        print("초미세먼지 농도는 " + fine_ultra_dust + "로 " + fu_state + " 상태입니다.")
        time.sleep(1)
        print("오존은 " + ozone + "으로 " + o_state + " 상태입니다.")
        print()
        time.sleep(1)

    dress(temperature)


def dress(temp):
    temp = int(temp)
    print("< 파이썬 챗봇의 오늘 코디 추천 >")
    if temp >= 27:
        print("으아..날씨가 너무 더워요! 반팔 반바지 시원하게 입고, 물 자주 챙겨 마셔요~")
    elif temp in range(20, 27):
        print("날씨가 제법 더워요! 반팔에 얇은 셔츠나 가디건 하나 챙기시는 것은 어떤가요~?")
    elif temp in range(12, 20):
        print("날씨가 제법 선선해요! 얇은 니트나 맨투맨을 추천드려요~")
    elif temp in range(9, 12):
        print("날씨가 조금 쌀쌀해요! 자켓, 트렌치코트로 멋내기 좋아요~")
    elif temp in range(5, 9):
        print("날씨가 조금 추워요! 포근한 니트에 코트 챙겨 입으세요~")
    else:
        print("날씨가 엄청 추워요! 패딩이나 두꺼운 코트 입고 나가세요~")


def rain(rate1, rate2):
    now = time.strftime('%H')
    if int(now) < 12:
        if (int(rate1) > 50 | int(rate2) > 50):
            print("오늘 비가 올 것 같아요. 우산을 챙기세요!")
    elif int(now) >= 12:
        if int(rate2) > 50:
            print("오늘 오후에 비가 올 것 같아요. 우산을 챙기세요")
