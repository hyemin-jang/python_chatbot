import pandas as pd
import time
import random

# main import
import main as m

def select_menu():
    print('========================================== 랜덤 메뉴 추천 ===========================================')
    inputed_num1 = input("1: 메뉴 추천받기 \t 2: 메뉴 추가하기 \n")
    if inputed_num1 == '1':
        random_menu()
    elif inputed_num1 == '2':
        add_menu()
    else:
        print("\n잘못 입력하셨습니다. 다시 입력해주세요.\n")
        time.sleep(1)
        select_menu()

inputed_type=None 
inputed_name=None
def add_menu():
    global inputed_type, inputed_name
    inputed_type = input("한식, 중식, 일식, 양식, 아시아 중 하나를 선택해주세요 : ")
    inputed_name = input("\n음식 이름을 입력해주세요 : ")
    inputed_num2 = input("\n추가되었습니다 \n 1: 메뉴 다시 추가하기 \t 2: 메뉴 추천받기 \t 3: 종료하기 ")
    if inputed_num2 == '1':
        add_menu()
    elif inputed_num2 == '2':
        random_menu()
    elif inputed_num2 == '3':
        endSelect()
    else:
        print("\n잘못 입력하셨습니다. 다시 입력해주세요.\n")
        time.sleep(1)
        add_menu()


def random_menu():
    query = '''
    select distinct foodname, foodtype
    from foodlist
    where foodname is not null
    '''
    df = pd.read_sql(query, m.connection)

    food_lists = {
        "한식": list(df[df.FOODTYPE == '한식']['FOODNAME']),
        "중식": list(df[df.FOODTYPE == '중식']['FOODNAME']),
        "일식": list(df[df.FOODTYPE == '일식']['FOODNAME']),
        "양식": list(df[df.FOODTYPE == '양식']['FOODNAME']),
        "아시아": list(df[df.FOODTYPE == '아시아']['FOODNAME']),
        "랜덤": list(df['FOODNAME'])
    }
    print('\n======================== 메뉴를 추천해드릴게요 ======================')
    inputed_menu = input("한식, 중식, 일식, 양식, 아시아, 랜덤 중 하나를 선택해주세요 : ")
    if inputed_menu in food_lists:
        food = random.choice(food_lists[inputed_menu])
        print('\n오늘의 점심은 ~~??\n')
        time.sleep(2)
        print(food + '입니다!!\n')
        select_after()
    else:
        print("\n잘못 입력하셨습니다. 다시 입력해주세요.\n")
        time.sleep(1)
        random_menu()



def select_after():
    inputed_num3 = input("1: 밥 값 내기 사다리 타기 \t 2: 다시선택하기 \t 3: 종료하기\n")
    if inputed_num3 == '1':
        game()
        endSelect()
    elif inputed_num3 == '2':
        select_menu()
    elif inputed_num3 == '3':
        endSelect()
    else:
        print("\n잘못 입력하셨습니다. 다시 입력해주세요.\n")
        time.sleep(1)
        select_after()


def game():
    name_list = input("참가자들의 이름을 입력해주세요 : ").split()
    winner = random.choice(name_list)
    for i in range(3, 0, -1):
        time.sleep(1)
        print(i)
    time.sleep(1)
    print('오늘은 ' + winner + '(이)가 쏜다!!')

def endSelect():
    time.sleep(1)
    print("식사 맛있게 하세요~~")
    