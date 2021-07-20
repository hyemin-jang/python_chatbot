import pandas as pd
import main as m 
import time


def list_dbInfo():
    time.sleep(2)
    user_input = input("옵션을 선택하세요: 택1) 플레이 많이 한 회원 확인 || 택2) 개인 별 게임 스코어 랭킹 확인하기 || 택3) 메뉴로 돌아가기: ")
    while (user_input != "1" and user_input != "2" and  user_input != "3"):
        time.sleep(2)
        user_input = input("잘못된 입력값입니다. 옵션을 선택하세요: 택1) 플레이 많이 한 회원 확인 || 택2) 개인 별 게임 스코어 랭킹 확인하기 || 택3) 메뉴로 돌아가기: ")
    
    while user_input != '3':
        if user_input == '1':
             check_player_time()
             user_input = input("옵션을 선택하세요: 택1) 플레이 많이 한 회원 확인 || 택2) 개인 별 게임 스코어 랭킹 확인하기 || 택3) 메뉴로 돌아가기: ")
        elif user_input == '2':
             rank_player_score()
             user_input = input("옵션을 선택하세요: 택1) 플레이 많이 한 회원 확인 || 택2) 개인 별 게임 스코어 랭킹 확인하기 || 택3) 메뉴로 돌아가기: ")
        else:
            time.sleep(2)
            user_input = input("잘못된 입력값입니다. 옵션을 선택하세요: 택1) 플레이 많이 한 회원 확인 || 택2) 개인 별 게임 스코어 랭킹 확인하기 || 택3) 메뉴로 돌아가기: ")
    
    return "DB 조회를 종료합니다."


def check_player_time():
    query = '''select * from chatbot'''
    #connection = cx_Oracle.connect(user='ora01', password='oracle_4U2021', dsn='mydb_high')
    df_chatbot = pd.read_sql(query, m.connection)  
    name_count = dict()

    
    for user_name in df_chatbot['USERNAME']:
        if user_name is not None:
            user_name = user_name.strip().upper()
        
            if user_name not in name_count:
                name_count[user_name] = 1
            else:
                name_count[user_name] += 1
                
    print("플레이 횟수가 가장 많은 유저부터 순서대로 알려드립니다. (단 플레이 횟수가 1회 초과로 범위를 제한합니다)")
    
    sort_player_frequency = sorted(name_count.items(), key = lambda x:x[1])
    
    
    
    for 이름, 횟수 in reversed(sort_player_frequency):
        if 횟수 > 1:
            time.sleep(1)
            print("플레이어 {0}님, 총 {1}회 실행하였습니다".format(이름, 횟수))
            
def rank_player_score():
    #connection = cx_Oracle.connect(user='ora01', password='oracle_4U2021', dsn='mydb_high')
    query = '''select * from chatbot where (USERNAME is not null) AND (JOINTIME is not null) AND (LOCATION is not null) AND (GAMESCORE is not null)  order by GAMESCORE desc'''
    df_chatbot = pd.read_sql(query, m.connection)
    
    for i in range(len(df_chatbot)):
        등수 = str(i+1) + "등:"
        이름 =df_chatbot['USERNAME'][i].upper() + "님"
        스코어 = "총 스코어: " + str(df_chatbot['GAMESCORE'][i])
        현시각 = "플레이 시간: " + df_chatbot['JOINTIME'][i].strftime('%Y-%m-%d %H:%M:%S')
        line_new = '{:^3} {:^15}|| {:^15} || {:^15}'.format(등수, 이름, 스코어, 현시각)
        time.sleep(1)
        print(line_new)
        
