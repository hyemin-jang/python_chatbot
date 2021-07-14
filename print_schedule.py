import pandas as pd
from datetime import datetime
import os
from urllib import request
from pathlib import Path
import gdown
 
url = 'https://drive.google.com/file/d/1bMP5JUjnCyQCG9-t_OiWfLdy2Msk8n_e/view'
output = '인공지능을 활용한 웹 서비스 개발자 양성과정 (12기)_커리큘럼.xlsx'
gdown.download(url, output, quiet=False)

#cmd 내 필요한 커맨드 키 
#pip install pandas
#pip install xrld
#pip install beautifulsoup4                   



    
def print_schedule():
    
    
    downloads_path = str(Path.home() / "Downloads") + "\\" + output
    print(downloads_path)
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
            print("오늘은 {0}입니다.".format(now))
            print('오늘의 플레이데이터 교육 일수는 {0}일차로, 이번 주차 과목 주제는 {1}이고, 해당 과목 세부 주제는 {2} 입니다.'.format(일수, 주제, 세부))
            break

    print('수료까지', 수료식.days,'일 남았습니다')
print_schedule()
