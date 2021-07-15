import pandas as pd
from datetime import datetime
import os
import urllib.request
from pathlib import Path
import time


# cmd 내 필요한 커맨드 키
# pip install pandas
# pip install xrld
# pip install os
# pip install datetime
# pip install requests
# pip install pathlib


url = "https://blog.kakaocdn.net/dn/b1lTSN/btq9zFt84zP/RxpfvHb8bQCqzcuXHIYKf0/%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%EC%9D%84%2B%ED%99%9C%EC%9A%A9%ED%95%9C%2B%EC%9B%B9%2B%EC%84%9C%EB%B9%84%EC%8A%A4%2B%EA%B0%9C%EB%B0%9C%EC%9E%90%2B%EC%96%91%EC%84%B1%EA%B3%BC%EC%A0%95%2B%2812%EA%B8%B0%29_%EC%BB%A4%EB%A6%AC%ED%81%98%EB%9F%BC.xlsx?attach=1&knm=tfile.xlsx"
urllib.request.urlretrieve(url, "인공지능을 활용한 웹 서비스 개발자 양성과정 (12기)_커리큘럼.xlsx")


def print_schedule():
    downloads_path = os.path.abspath(
        "인공지능을 활용한 웹 서비스 개발자 양성과정 (12기)_커리큘럼.xlsx")
    schedule = pd.read_excel(downloads_path)
    now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    END_DATE = datetime(2021, 12, 27, 18, 0, 0)
    수료식 = END_DATE - datetime.now()

    for i in range(len(schedule)):
        일자 = schedule.values[i][0]
        일수 = schedule.values[i][1]
        주제 = schedule.values[i][2]
        세부 = schedule.values[i][3]
        if (now == 일자):
            time.sleep(1)
            print("오늘은 {0}입니다.".format(now))
            time.sleep(1)
            print('오늘의 플레이데이터 교육 일수는 {0}일차로, 이번 주차 과목 주제는 {1}이고, 해당 과목 세부 주제는 {2} 입니다.'.format(
                일수, 주제, 세부))
            break
    time.sleep(1)
    print('수료까지', 수료식.days, '일 남았습니다')
print_schedule()
