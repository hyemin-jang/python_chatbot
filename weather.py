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

# # 미세먼지
# #fine_dust = soup.select('dl.indicator > dd > span.num')[0].get_text()
# f_data = soup.select('dl.indicator > dd')[0].get_text()
# idx = f_data.find("㎥")
# fine_dust = f_data[:idx+1]
# f_state = f_data[idx+1:]

# # 초미세먼지
# #fine_ultra_dust = soup.select('dl.indicator > dd > span.num')[1].get_text()
# fu_data = soup.select('dl.indicator > dd')[1].get_text()
# idx = fu_data.find("㎥")
# fine_ultra_dust = fu_data[:idx+1]
# fu_state = fu_data[idx+1:]

# # 오존
# #ozone = soup.select('dl.indicator > dd > span.num')[2].get_text()
# o_data = soup.select('dl.indicator > dd')[2].get_text()
# idx = o_data.find("m")
# ozone = o_data[:idx+1]
# o_state = o_data[idx+1:]


def dustOzone():
    n_list = []
    s_list = []
    sep = ["㎥", "㎥", "m"]

    for i in range(3):
        data = soup.select('dl.indicator > dd')[i].get_text()
        idx = data.find(sep[i])
        if idx != -1:
            n_list.append(data[:idx+1])
            s_list.append(data[idx+1:])
        else:
            break

    return n_list, s_list


dustOzone
print(dustOzone()[0][0])
print(len(dustOzone()[0]))


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

    dustOzone()

    if (len(dustOzone()[0]) == 3) & (len(dustOzone()[1]) == 3):
        print("미세먼지 농도는 {}로 {} 상태이고,".format(
            dustOzone()[0][0], dustOzone()[1][0]))
        time.sleep(1)
        print("초미세먼지 농도는 {}로 {} 상태입니다.".format(
            dustOzone()[0][1], dustOzone()[1][1]))
        time.sleep(1)
        print("오존은 {}으로 {} 상태입니다.".format(
            dustOzone()[0][2], dustOzone()[1][2]))

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
    now = time.strftime('%H')
    if int(now) < 12:
        if (rate1 > 50 | rate2 > 50):
            print("오늘 비가 올 것 같아요. 우산을 챙기세요!")
    elif int(now) >= 12:
        if rate2 > 50:
            print("오늘 오후에 비가 올 것 같아요. 우산을 챙기세요")
