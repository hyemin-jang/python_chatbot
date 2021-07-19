import time

# 각각 기능 담은 파일 import
import alarm as al
import weather as wt
import schedule_check as sc
import menuselect as ms
import minigame as mg
import corona as cn
import news as n

# db 연동에 필요한 패키지 import
import pandas as pd
import cx_Oracle
from datetime import datetime


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


def startChat():
    time.sleep(1)
    print("============================== start! ==============================")
    print("안녕하세요. 채팅을 시작합니다.")
    time.sleep(1)

    al.qrcheck()
    time.sleep(1)
    global name
    name = input("\n이름을 입력해주세요.\n")
    check = time.localtime()
    now = datetime.now()

    # db연동
    cx_Oracle.init_oracle_client(
        lib_dir=r"C:\playdata\oracle\instantclient_19_11")
    connection = cx_Oracle.connect(
        user='ora01', password='oracle_4U2021', dsn='mydb_high')

    cursor = connection.cursor()

    sql = 'insert into chatbot values (:chatbotName, :rightNow)'
    cursor.execute(sql, chatbotName=name, rightNow=now)

    connection.commit()
    cursor.close()
    connection.close()

    choose()


def endChat():
    time.sleep(1)
    print("다음에 이야기 나눠요~!")
    print("============================== end! ==============================")


def choose():
    print()
    time.sleep(1)
    print(name + "님, 무엇을 도와드릴까요?")
    time.sleep(1)

    print("실행하고 싶은 메뉴 번호를 입력해주세요.")
    time.sleep(1)

    global cnum
    cnum = input(
        "1:날씨 정보 \t 2:플레이데이터 시간표 \t 3:점심메뉴 고르기\n4:미니게임 \t 5: 코로나 확진 현황 \t 6: 오늘의 뉴스 정보\t 999: 챗봇 종료\n")

    clist = ["1", "2", "3", "4", "5", "6"]
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

    print()
    time.sleep(1)
    print("----------------------------------------"*3)
    time.sleep(1)
    choose()
