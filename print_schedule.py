import pandas as pd
from datetime import datetime
import os
import urllib.request
import time


# cmd 내 필요한 커맨드 키
# pip install pandas
# pip install xrld
# pip install os
# pip install datetime
# pip install requests




def hours_minutes_seconds(time_left):
    time_left = datetime.strptime(str(time_left), "%H:%M:%S")
    
    
    return time_left.hour, time_left.minute, time_left.second


def check_time_left(right_now):
    right_now = right_now.replace(microsecond = 0)
    아침시간 = right_now.replace(hour = 9, minute = 0, second = 0, microsecond = 0)
    점심시간 = right_now.replace(hour = 13, minute = 0, second = 0, microsecond = 0)
    종강시간 = right_now.replace(hour = 18, minute = 0, second = 0, microsecond = 0)

    if right_now < 아침시간:
        시차 = 아침시간 - right_now
        시간, 분, 초 = hours_minutes_seconds(시차)
        print("수강 전이고 수강 시작까지 {0}시 {1}분 {2}초 남았습니다. 아침 먹고 공부할 준비 하세요!".format(시간, 분, 초))

    elif 아침시간 < right_now < 점심시간:
        시차 = 점심시간 - right_now
        시간, 분, 초 = hours_minutes_seconds(시차)
        print("점심시간까지 {0}분 {1}분 {2}초 남았습니다. 조금만 더 힘내세요!".format(시간, 분, 초))


    elif (점심시간 < right_now < 종강시간):
        시차 = 종강시간 - right_now 
        시간, 분, 초 = hours_minutes_seconds(시차)
        print("퇴실까지 {0}시 {1}분 {2}초 남았습니다. 조금만 더 힘내세요!".format(시간, 분, 초))
    else:
      # 시차 = right_now - 종강시간
      # 시간, 분, 초 = hours_minutes_seconds(시차)
        print("고생하셨습니다. 오늘 한 것들 잘 마무리 해주시고 다음 수업 준비해주세요!")


def download_file_and_open_excel():
    PLAYDATA_FILE =  "인공지능을 활용한 웹 서비스 개발자 양성과정 (12기)_커리큘럼.xlsx"
    url = "https://blog.kakaocdn.net/dn/b1lTSN/btq9zFt84zP/RxpfvHb8bQCqzcuXHIYKf0/%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%EC%9D%84%2B%ED%99%9C%EC%9A%A9%ED%95%9C%2B%EC%9B%B9%2B%EC%84%9C%EB%B9%84%EC%8A%A4%2B%EA%B0%9C%EB%B0%9C%EC%9E%90%2B%EC%96%91%EC%84%B1%EA%B3%BC%EC%A0%95%2B%2812%EA%B8%B0%29_%EC%BB%A4%EB%A6%AC%ED%81%98%EB%9F%BC.xlsx?attach=1&knm=tfile.xlsx"
    urllib.request.urlretrieve(url,  PLAYDATA_FILE) # 인공지능을 활용한 웹 서비스 개발자 양성과정 파일 명을 url에서 다운받는 라이브러리
    
    
    find_schedule_excel_location = os.path.abspath("인공지능을 활용한 웹 서비스 개발자 양성과정 (12기)_커리큘럼.xlsx")  # 현재 디렉토리 위치에 있는 파일명과 디렉토리 주소를 가져옴
    grab_schedule = pd.read_excel(find_schedule_excel_location)  # 가져온 디렉토리 명내 파일 읽음 
    return grab_schedule
    
    


def print_schedule():
    schedule = download_file_and_open_excel()

    now = datetime.now().strftime("%Y-%m-%d")
    END_DATE = datetime(2021, 12, 27, 18, 0, 0)
    수료식 = END_DATE - datetime.now() #수료식까지 완료날에서부터 오늘날까지 값을 빼는 계산


    for i in range(len(schedule)):
        일자 = schedule.values[i][0].strftime("%Y-%m-%d")  #20xx-xx-xx
        일수 = schedule.values[i][1]
        주제 = schedule.values[i][2]
        세부 = schedule.values[i][3]
        
        월일년 = 일자.split('-')
    
        
        if (now == 일자):
            time.sleep(1)
            print("오늘은 {0}년 {1}월 {2}일입니다.".format(월일년[0], 월일년[1], 월일년[2]))


            time.sleep(1)
            print("오늘의 플레이데이터 교육 일수는 {0}일차로, 이번 주차 과목 주제는 {1}이고, ".format(int(일수), 주제))


            time.sleep(1)
            print("해당 과목 세부 주제는 {0} 입니다.".format(세부))
            
            time.sleep(1)
            check_time_left(datetime.now())
            
            break

    time.sleep(1)
    print('수료까지', 수료식.days, '일 남았습니다')
    

def study_in_advance():
    study_date = input("선행학습 내용을 알고싶은 날짜를 알려주세요! [단, 20xx-xx-xx 형식으로 기재해주세요.] : ")
    
    check = {}
    
    while True: # study_date의 형식이 올바른 지 확인합니다. 
        for char in study_date:
            if char in check.keys():
                check[char] += 1
            else:
                check[char] = 1
        try:
            if check['-'] == 2:
                check_list = study_date.split('-')
                if len(check_list[0]) == 4 and len(check_list[1]) == 2 and len(check_list[2]) == 2 and check_list[0].isdigit() and check_list[1].isdigit() and check_list[2].isdigit():
                    년, 월, 일 = int(check_list[0]), int(check_list[1]), int(check_list[2])
                    print("기입된 정보 확인했습니다. {0}년 {1}월 {2}일 데이터 정보 확인해보겠습니다.".format(년, 월, 일))
                    break
        except:
            print("잘못된 형식의 기입입니다. 날짜 형식을 20xx-xx-xx 형태로 알려주세요: ", end = "" )
            study_date = input()
    
    schedule = download_file_and_open_excel()
    
    for i in range(len(schedule)):
        일자 = schedule.values[i][0].strftime("%Y-%m-%d")  #20xx-xx-xx
        일수 = schedule.values[i][1]
        주제 = schedule.values[i][2]
        세부 = schedule.values[i][3]                
    
        if (study_date == 일자):
            time.sleep(1)
            print("해당 일수의 플레이데이터 교육 일수는 {0}일차로, 해당 주 과목 주제는 {1}이고, ".format(int(일수), 주제))

            time.sleep(1)
            print("해당 주 과목 세부 주제는 {0} 입니다.".format(세부))
            
            break
        
    if study_date != 일자:
        time.sleep(1)
        print("입력한 날짜의 데이터는 엑셀 파일 내에 존재하지 않습니다.")
    
        