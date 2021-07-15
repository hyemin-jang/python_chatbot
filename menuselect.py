import pandas as pd
from datetime import datetime
import os


def get_file(drive_location, filename="인공지능을 활용한 웹 서비스 개발자 양성과정 (12기)_커리큘럼.xlsx"):

    path2 = os.path.dirname(drive_location + ":/")
    FINDING_FILE: Final = "인공지능을 활용한 웹 서비스 개발자 양성과정 (12기)_커리큘럼.xlsx"

    return file_path


# cmd 내 필요한 커맨드 키
# pip install pandas
# pip install xrld
# pip install beautifulsoup4

def print_schedule():

    start_from_A = 65

    up_until_Z = 26

    alphabet_list = [chr(start_from_A) for start_from_A in range(
        start_from_A, start_from_A + up_until_Z) if (start_from_A) <= ord('z')]

    drive_location = input("사용하는 드라이브 명을 기입해주세요 [예: C, D, E, F, ... ]")

    while (drive_location.upper() not in alphabet_list):
        print("올바른 드라이브 명을 입력하세요: ")
        drive_location = input()
    # drive_location을 이용해서 새 함수로 드라이버 첫 번째부터 시작해서 import os로 파일 찾는 구현

    # if 파일이 없음 경우 -> 파일 다운로드 구현
        # url = "https://www.notion.so/5d13426d3675461c953a8663d5670f40#56f1d5cd162b445890cc389a6d9b7e3a";
        # saved_file_name = "인공지능을 활용한 웹 서비스 개발자 양성과정 (12기)_커리큘럼.xlsx"
        # urllib.request.urlretrieve(url, saved_file_name)

    schedule = pd.read_excel(
        'C:/Users/USER/Downloads/인공지능을 활용한 웹 서비스 개발자 양성과정 (12기)_커리큘럼.xlsx')
    now = datetime.now()
    now = now.replace(hour=0, minute=0, second=0, microsecond=0)
    for i in range(len(schedule['일자'])):
        if (now == schedule['일자'][i]):
            #print("오늘은 {0}입니다.".format(now))
            print('오늘의 플레이데이터 교육 일수는 {0}일차로, 배울 과목 주제는 {1}이고, 해당 과목 세부 주제는 {2} 입니다.'.format(
                schedule['일수'][i], schedule['주제'][i], schedule['세부'][i]))
            # 날짜, 요일, 플레이데이터 완강까지 몇 일 남음.
            break


print_schedule()
