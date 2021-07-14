import time
import weather as wt


def startChat():
    global answer  # answer를 전역변수로 설정
    answer = input("채팅을 시작하시겠습니까?  Y or N\n")

    if answer == "Y":
        print("=============== start! ===============")
        print("안녕하세요. 채팅을 시작합니다.")
        time.sleep(1)

        global name  # 이름을 전역변수로 설정
        name = input("이름을 입력해주세요.\n")

    elif answer == "N":
        endChat()

    else:
        print("Y 혹은 N로 대답해주세요.\n")
        time.sleep(1)
        startChat()


def endChat():
    time.sleep(1)
    print("다음에 이야기 나눠요~!")
    print("=============== end! ===============")


def choose():
    print()
    print(name + "님, 무엇을 도와드릴까요?")
    time.sleep(1)
    print("1:날씨 정보 \t 2:플레이데이터 시간표 \t 3:점심메뉴 고르기 \t 4:미니게임 \t 999: 챗봇 종료")
    time.sleep(1)

    cnum = input("실행하고 싶은 메뉴 번호를 입력해주세요.\n")

    if cnum == "1":
        print("\n날씨 시작")
        time.sleep(1)
        wt.weather()
    elif cnum == "2":
        print("\n시간표 시작")
        # timetable()
    elif cnum == "3":
        print("\n점심메뉴 시작")
        # lunch()
    elif cnum == "4":
        print("\n미니게임 시작")
        # minigame()
    elif cnum == "999":
        endChat()
    else:
        print("\n잘못 입력하셨습니다. 다시 입력해주세요.")
        time.sleep(1)
        choose()


startChat()
choose()
