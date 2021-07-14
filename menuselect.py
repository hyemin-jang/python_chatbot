import time
import random

def game():
    name_list = list(map(str, input("이름을 입력해주세요 : ").split()))
    winner= random.choice(name_list)
    for i in range(3, 0, -1):
        time.sleep(1)
        print(i)
    time.sleep(1)
    print('오늘은 ' + winner + '이가 쏜다!!')


def menu():  #딕셔너리사용
    food_lists = { 
        "한식" : ['비빔밥','김치찌개','불고기'],
        "중식" : ['짜장면','짬뽕','새우볶음밥'],
        "일식" : ['초밥','우동','가츠동'],
        "양식" : ['파스타','피자','리조또'],
        "아시아" : ['마라탕','쌀국수','팟타이'],
        "랜덤" : ['햄버거','라면','국수']
    # 엑셀 파일로 만들어서 가져와보기
    }   

    print("=============== 점심 메뉴를 추천해드릴게요 ===============")
    inputed_menu = input("한식, 중식, 일식, 양식, 아시아, 랜덤 중 하나를 선택해주세요 : ")
   
    for selected_menu in food_lists:
        if inputed_menu == selected_menu:
            category = inputed_menu
            food = random.choice(food_lists[category])
            print('오늘의 점심은 ~~??\n')
            time.sleep(2)
            print(food + '입니다!!\n')

            inputed_num = input("1: 밥 값 내기 사다리 타기 \t 2: 다시선택하기 \t 3: 종료하기\n")
            if inputed_num == '1':
                game()
                endSelect()
            if inputed_num == '2':
                menu()
                endSelect()
            else:
                endSelect()
    print("\n잘못 입력하셨습니다. 다시 입력해주세요.\n")
    time.sleep(1)
    menu()
   
def endSelect():
    time.sleep(1)
    print("식사 맛있게 하세요~~")
    print("=============== end! ===============")
    exit()


