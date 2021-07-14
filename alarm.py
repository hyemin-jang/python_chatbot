import datetime
import random
import webbrowser

now = datetime.datetime.now()

if now.hour < 9:
    driver = webbrowser.get()
    driver.open("https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbNxhPt%2Fbtq9zF0mmnP%2FjrvH2qea4yKPkMsvz4X7G1%2Fimg.jpg")
    print("현재 시간은 {}시! 아직 입실 안했다면 입실하세요.".format(now.hour))

# 퇴실
elif now.hour >= 18:
    driver = webbrowser.get()
    driver.open("https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbNxhPt%2Fbtq9zF0mmnP%2FjrvH2qea4yKPkMsvz4X7G1%2Fimg.jpg")
    print("현재 시간은 {}시! 아직 퇴실 안했다면 퇴실 하세요".format(now.hour))

# 그 외 시간
else:
    my_list = ["인생에 집중하세요", "많이 먹지마세요", "조심하세요", "돈을 빌리지 마세요", "좋은 연락이 옵니다"]
result = random.choice(my_list)
print(result)
