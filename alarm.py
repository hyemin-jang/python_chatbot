import datetime
import random
import webbrowser
now = datetime.datetime.now()


def qrcheck():

    def qropen():
        driver = webbrowser.get()
        driver.open("https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbNxhPt%2Fbtq9zF0mmnP%2FjrvH2qea4yKPkMsvz4X7G1%2Fimg.jpg")

    def fortune():
        my_list = ["인생에 집중하세요", "많이 먹지마세요",
                   "조심하세요", "돈을 빌리지 마세요", "좋은 연락이 옵니다"]
        result = random.choice(my_list)
        print("오늘의 운세 :", result)
    fortune()

    happytime = now.strftime('%H:%M')
    if "08:50" < happytime < "09:05":
        checker = input(
            "입실 완료하셨나요? \n아직 안했다면, QR코드를 보여드립니다. \n[아직 안함요- 1]  [이미 했음- 2] \n")
        if checker == "1":
            qropen()
        else:
            fortune()

    if "17:50" < happytime < "18:30":
        checker = input(
            "퇴실 완료하셨나요? \n아직 안했다면, QR코드를 보여드립니다. \n[아직 안함요- 1]  [이미 했음- 2] \n")
        if checker == "1":
            qropen()
        else:
            fortune()
