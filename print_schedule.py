import pandas as pd
from datetime import datetime

def print_schedule():
    df = pd.read_excel('C:/Users/USER/Downloads/인공지능을 활용한 웹 서비스 개발자 양성과정 (12기)_커리큘럼.xlsx')
    now = datetime.now()
    now = now.replace(hour = 0, minute = 0, second = 0, microsecond = 0)
    for i in range(len(df['일자'])):
        if (now == df['일자'][i]):
            print('오늘의 일수차는 {0}, 과목 주제는 {1}, 해당 과목 세부 주제는 {2} 입니다.'.format(df['일수'][i], df['주제'][i], df['세부'][i]))
            break;
    
print_schedule()
