import datetime
import random
import webbrowser
now = datetime.datetime.now()


def qrcheck():

    def qropen():
        driver = webbrowser.get()
        driver.open("https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbNxhPt%2Fbtq9zF0mmnP%2FjrvH2qea4yKPkMsvz4X7G1%2Fimg.jpg")

    def fortune():
        my_list = ["극심한 슬럼프는 성공의 전단계다.", "담을 수 있는 그릇을 키운다면\n 그 그릇이 채워지는 건 단지 시간 차이일 뿐이다.", "걱정하지마! 잘하고 있어",
                   "단순하고 멍청하게 대항하는 것이\n 두려움 극복의 지름길이다.", "삶은 실수투성이야, 우리는 늘 실수를 하지.\n - 영화 '주토피아'", "좋은 연락이 옵니다"]
        result = random.choice(my_list)
        print("오늘의 명언\n :", result)
    fortune()

    happytime = now.strftime('%H:%M')
    if "08:50" < happytime < "09:05":
        checker = input(
            "입실 완료하셨나요? \n아직 안했다면, QR코드를 보여드립니다. \n[아직 안함요- 1]  [이미 했음- 2] \n")
        if checker == "1":
            qropen()
        else:
            fortune()

    elif "17:50" < happytime < "18:30":
        checker = input(
            "퇴실 완료하셨나요? \n아직 안했다면, QR코드를 보여드립니다. \n[아직 안함요- 1]  [이미 했음- 2] \n")
        if checker == "1":
            qropen()
        else:
            fortune()
