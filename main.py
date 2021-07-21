import time
from datetime import datetime

# db 연동에 필요한 패키지 import
import cx_Oracle

# 각각 기능 담은 파일 import
import alarm as al
import weather as wt
import schedule_check as sc
import menuselect as ms
import minigame as mg
import corona as cn
import news as n
import check_db_info as di

# db 연동
import dbconnect as db


def db_connect():
    global connection, cursor
    cx_Oracle.init_oracle_client(
        lib_dir="C:\oracle\instantclient_19_11")
    connection = cx_Oracle.connect(
        user='ora01', password='oracle_4U2021', dsn='mydb_high')
    cursor = connection.cursor()
    chatbot()


def chatbot():
    answer = input("채팅을 시작하시겠습니까?  Y or N\n")

    if answer in ["Y", "y"]:
        startChat()

    elif answer in ["N", "n"]:
        endChat()

    else:
        time.sleep(1)
        print("Y 혹은 N로 대답해주세요.\n")
        time.sleep(1)
        chatbot()


name = None


def startChat():
    time.sleep(1)
    start = " start! "
    print("="*((100-len(start))//2) + start + "="*((100-len(start))//2))
    print("안녕하세요. 채팅을 시작합니다.")
    time.sleep(1)

    al.qrcheck()
    time.sleep(1)

    global name, now

    name = input("이름을 입력해주세요.\n").replace(" ", "")
    now = datetime.now()

    choose()


def endChat():
    time.sleep(1)
    print("다음에 이야기 나눠요~!")
    end = " end! "
    print("="*((100-len(end))//2) + end + "="*((100-len(end))//2))

    if (name):
        db.db_insert_data()


def choose():
    time.sleep(1)
    print("\n" + name + "님, 무엇을 도와드릴까요?")
    time.sleep(1)

    print("실행하고 싶은 메뉴 번호를 입력해주세요.")
    time.sleep(1)

    global cnum
    cnum = input(
        "1:날씨 정보 \t 2:플레이데이터 시간표 \t 3:점심메뉴 고르기\n4:미니게임 \t 5: 코로나 확진 현황 \t 6: 오늘의 뉴스 정보\t 7: 플레이 유저 정보 조회\t 999: 챗봇 종료\n")

    clist = ["1", "2", "3", "4", "5", "6", "7"]
    if cnum in clist:
        func()
    elif cnum == "999":
        endChat()
    else:
        print("메뉴 번호를 잘못 입력하셨습니다.")
        time.sleep(1)
        choose()


def func():

    if cnum == "1":
        time.sleep(1)
        wt.weather()
    elif cnum == "2":
        time.sleep(1)
        sc.schedule_check()
    elif cnum == "3":
        time.sleep(1)
        ms.select_menu()
    elif cnum == "4":
        time.sleep(1)
        mg.miniGame()
    elif cnum == "5":
        time.sleep(1)
        cn.corona()
    elif cnum == "6":
        time.sleep(1)
        n.todayNews()
    elif cnum == "7":
        time.sleep(1)
        di.list_dbInfo()
    print()
    time.sleep(1)
    print("===================="*5)
    time.sleep(1)
    choose()
