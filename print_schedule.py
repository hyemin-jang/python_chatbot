import pandas as pd
from datetime import datetime
import os
import urllib.request
from pathlib import Path
import time
 

#cmd 내 필요한 커맨드 키 
#pip install pandas
#pip install xrld
#pip install os
#pip install datetime
#pip install requests
#pip install pathlib


url = "https://blogattach.naver.com/35a0299a8bd1d10d21c5a094aa443146eabc41a7df/20210715_232_blogfile/rudqo0913_1626286527382_eNu8d0_xlsx/%C0%CE%B0%F8%C1%F6%B4%C9%C0%BB+%C8%B0%BF%EB%C7%D1+%C0%A5+%BC%AD%BA%F1%BD%BA+%B0%B3%B9%DF%C0%DA+%BE%E7%BC%BA%B0%FA%C1%A4+%2812%B1%E2%29_%C4%BF%B8%AE%C5%A7%B7%B3.xlsx"
urllib.request.urlretrieve(url,"인공지능을 활용한 웹 서비스 개발자 양성과정 (12기)_커리큘럼.xlsx" )

    
def print_schedule(): 
    downloads_path = os.path.abspath("인공지능을 활용한 웹 서비스 개발자 양성과정 (12기)_커리큘럼.xlsx")
    schedule = pd.read_excel(downloads_path)
    now = datetime.now().replace(hour = 0, minute = 0, second = 0, microsecond = 0)

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
            print('오늘의 플레이데이터 교육 일수는 {0}일차로, 이번 주차 과목 주제는 {1}이고, 해당 과목 세부 주제는 {2} 입니다.'.format(일수, 주제, 세부))
            break
    time.sleep(1)
    print('수료까지', 수료식.days,'일 남았습니다')
print_schedule()
