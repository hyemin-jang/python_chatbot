from bs4 import BeautifulSoup
import requests
import time

html = requests.get('https://search.naver.com/search.naver?query=날씨')

soup = BeautifulSoup(html.text, 'html.parser')


# 현재 위치, 기온 찾기
location = soup.select('span.btn_select > em')[0].get_text()
temperature = int(soup.select('.todaytemp')[0].get_text())

# 강수 확률
rain_rate1 = int(soup.select('span.point_time > span.rain_rate > span.num')[
    0].get_text())
rain_rate2 = int(soup.select('span.point_time > span.rain_rate > span.num')[
    1].get_text())


# 미세먼지, 초미세먼지, 오존
n_list = []
s_list = []
sep = ["㎥", "㎥", "m"]

for i in range(3):
    if len(soup.select('dl.indicator > dd') == 3:
        data=soup.select('dl.indicator > dd')[i].get_text()
        idx=data.find(sep[i])
        if idx != -1:
            n_list.append(data[:idx+1])
            s_list.append(data[idx+1:])
        else:
            break
    else:
        break


def weather():
    print("지금 계신 {}의 날씨를 알려드릴게요. 잠시만 기다려주세요\b".format(location))
    print()
    time.sleep(2)
    print("현재 {}의 기온은 {}℃ 입니다.".format(location, temperature))
    time.sleep(1)
    print("오전 강수 확률은 {}%이고, 오후 강수 확률은 {}%입니다.".format(rain_rate1, rain_rate2))
    time.sleep(1)

    rain(rain_rate1, rain_rate2)

    time.sleep(1)

    if (len(n_list) == 3) & (len(s_list) == 3):
        print("미세먼지 농도는 {}로 {} 상태이고,".format(
            n_list[0], s_list[0]))
        time.sleep(1)
        print("초미세먼지 농도는 {}로 {} 상태입니다.".format(
            n_list()[1], s_list[1]))
        time.sleep(1)
        print("오존은 {}으로 {} 상태입니다.".format(
            n_list()[2], s_list[2]))

    time.sleep(1)
    dress(temperature)


def dress(temp):
    print()
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
    now=time.strftime('%H')
    if int(now) < 12:
        if (rate1 > 50 or rate2 > 50):
            print("오늘 비가 올 것 같아요. 우산을 챙기세요!")
        else:
            print("오늘은 비가 올 것 같지 않네요!")
    else:
        if rate2 > 50:
            print("오늘 오후에 비가 올 것 같아요. 우산을 챙기세요")
        else:
            print("오늘 오후에는 비가 올 것 같지 않네요")
