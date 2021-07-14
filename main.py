import time

# 각각 기능 담은 파일 호출
import alarm as al
import weather as wt
# 시간표
import menuselect as ms
import minigame as mg
import corona as cn


def startChat():
    global answer
    answer = input("채팅을 시작하시겠습니까?  Y or N\n")

    if answer == "Y":
        print("============================== start! ==============================")
        print("안녕하세요. 채팅을 시작합니다.")
        time.sleep(1)

        al.qrcheck()

        global name
        name = input("이름을 입력해주세요.\n")
        choose()

    elif answer == "N":
        endChat()

    else:
        time.sleep(1)
        print("Y 혹은 N로 대답해주세요.\n")
        time.sleep(1)
        startChat()


def endChat():
    time.sleep(1)
    print("다음에 이야기 나눠요~!")
    print("============================== end! ==============================")


def choose():

    print(name + "님, 무엇을 도와드릴까요?")
    time.sleep(1)

    global cnum
    print("실행하고 싶은 메뉴 번호를 입력해주세요.")
    time.sleep(1)

    cnum = input(
        "1:날씨 정보 \t 2:플레이데이터 시간표 \t 3:점심메뉴 고르기 \t 4:미니게임 \t 5: 코로나 확진 현황 \t 999: 챗봇 종료\n")

    clist = ["1", "2", "3", "4", "5", "999"]
    if cnum not in clist:
        print("메뉴 번호를 잘못 입력하셨습니다.")
        time.sleep(1)
        choose()
    else:
        func()


def func():
    if cnum in ["1", "2", "3", "4", "5"]:

        if cnum == "1":
            time.sleep(1)
            wt.weather()
        elif cnum == "2":
            print("\n시간표 시작")
            # timetable()
        elif cnum == "3":
            time.sleep(1)
            ms.menu()
        elif cnum == "4":
            time.sleep(1)
            mg.miniGame()
        elif cnum == "5":
            time.sleep(1)
            cn.corona()

        print()
        time.sleep(1)
        print("----------------------------------------"*3)
        time.sleep(1)
        choose()

    else:
        endChat()
