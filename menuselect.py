import pandas as pd
import time
import random


def game():
    name_list = list(map(str, input("이름을 입력해주세요 : ").split()))
    winner = random.choice(name_list)
    for i in range(3, 0, -1):
        time.sleep(1)
        print(i)
    time.sleep(1)
    print('오늘은 ' + winner + '이가 쏜다!!')


def retry():
    print("\n잘못 입력하셨습니다. 다시 입력해주세요.\n")
    time.sleep(1)
    select_menu()


def endSelect():
    time.sleep(1)
    print("식사 맛있게 하세요~~")
    print("=============== end! ===============")


def select_menu():
    df = pd.read_excel('food_list.xlsx')

    food_lists = {
        "한식": list(df['한식']),
        "중식": list(df['중식']),
        "일식": list(df['일식']),
        "양식": list(df['양식']),
        "아시아": list(df['아시아']),
        "랜덤": list(df['한식']) + list(df['중식']) + list(df['일식']) + list(df['양식']) + list(df['아시아'])
    }

    print("=============== 점심 메뉴를 추천해드릴게요 ===============")
    inputed_menu = input("한식, 중식, 일식, 양식, 아시아, 랜덤 중 하나를 선택해주세요 : ")
    if inputed_menu in food_lists:
        food = random.choice(food_lists[inputed_menu])
        print('오늘의 점심은 ~~??\n')
        time.sleep(2)
        print(food + '입니다!!\n')
        select_after()
    else:
        retry()


def select_after():
    inputed_num = input("1: 밥 값 내기 사다리 타기 \t 2: 다시선택하기 \t 3: 종료하기\n")
    if inputed_num == '1':
        game()
        endSelect()
    elif inputed_num == '2':
        select_menu()
        endSelect()
    elif inputed_num == '3':
        endSelect()
    else:
        print("\n잘못 입력하셨습니다. 다시 입력해주세요.\n")
        time.sleep(1)
        select_after()
