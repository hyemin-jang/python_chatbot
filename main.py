import time

# 각각 기능 담은 파일 호출
import alarm as al
import weather as wt
import print_schedule as ps
import menuselect as ms
import minigame as mg
import corona as cn


def chatbot():
    answer = input("채팅을 시작하시겠습니까?  Y or N\n")

    if answer == "Y":
        startChat()

    elif answer == "N":
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
    print()
    time.sleep(1)

    # al.qrcheck()

    time.sleep(1)
    global name
    name = input("이름을 입력해주세요.\n")
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
        "1:날씨 정보 \t 2:플레이데이터 시간표 \t 3:점심메뉴 고르기 \t 4:미니게임 \t 5: 코로나 확진 현황 \t 999: 챗봇 종료\n")

    clist = ["1", "2", "3", "4", "5", "999"]
    if cnum not in clist:
        print("메뉴 번호를 잘못 입력하셨습니다.")
        time.sleep(1)
        choose()
    else:
        func()


def func():
    # 기능 메뉴를 선택했다면
    if cnum in ["1", "2", "3", "4", "5"]:
        if cnum == "1":
            time.sleep(1)
            wt.weather()
        elif cnum == "2":
            time.sleep(1)
            ps.print_schedule()
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

    # 채팅 종료를 선택했다면
    else:
        endChat()
