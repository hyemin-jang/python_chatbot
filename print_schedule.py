import pandas as pd
from datetime import datetime
#import urllib.request
#import os
#from string import ascii_lowercase

#cmd 내 필요한 커맨드 키 
#pip install pandas
#pip install xrld
#pip install beautifulsoup4

def print_schedule():
    #drive_location = input("사용하는 드라이브 명을 기입해주세요 [예: C, D, E, F, ... ]")
    # alpha_list = list(ascii_lowercase) -> ['a', 'b', 'c', .... 'z']
    #while (drive_location.lower() not in alpha_list):
        #print("올바른 드라이브 명을 입력하세요: ")
        #drive_location = input()
    
    #drive_location을 이용해서 import os로 파일 찾는 구현
    
    # if 파일이 없음 경우 -> 파일 다운로드 구현
        # url = "https://www.notion.so/5d13426d3675461c953a8663d5670f40#56f1d5cd162b445890cc389a6d9b7e3a";
        # saved_file_name = "인공지능을 활용한 웹 서비스 개발자 양성과정 (12기)_커리큘럼.xlsx"
        # urllib.request.urlretrieve(url, saved_file_name)
    
    df = pd.read_excel('C:/Users/USER/Downloads/인공지능을 활용한 웹 서비스 개발자 양성과정 (12기)_커리큘럼.xlsx')
    now = datetime.now()
    now = now.replace(hour = 0, minute = 0, second = 0, microsecond = 0)
    for i in range(len(df['일자'])):
        if (now == df['일자'][i]):
            print('오늘자 플레이데이터 교육 일수는 {0}일차로, 배울 과목 주제는 {1}이고, 해당 과목 세부 주제는 {2} 입니다.'.format(df['일수'][i], df['주제'][i], df['세부'][i]))
            break;
    
print_schedule()
