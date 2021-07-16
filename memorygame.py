import random
import time


def memoryGame():
    level = [6, 8, 10]

    print('\n*********************** 기억력 테스트 게임 ***********************')
    time.sleep(1.5)
    print('숫자가 나온 순서대로 입력해주세요!')
    time.sleep(1.5)
    print('(숫자 사이 스페이스바, 완료 후 엔터)')
    time.sleep(1.5)

    for lv in level:
        print('시작!')
        time.sleep(2)
        printRandomNum(lv)
        user_input = input('정답 >> ')
        answerCheck(user_input, answer)

        if success == False:
            break
        if lv != level[-1]:
            print('다음 단계로 넘어갑니다.')
            time.sleep(1)

    print('게임이 끝났습니다 :)')


# 랜덤 숫자 생성해서 출력
def printRandomNum(lv):
    global answer
    answer = []
    for i in range(lv):
        n = random.randrange(0, 10)
        answer.append(n)
        print(' '*i, n, end='\r')
        time.sleep(0.5)
        print(' '*(lv+2), end='\r')


def answerCheck(user_input, answer):
    global success
    try:
        user_answer = list(map(int, user_input.strip().split(' ')))
        if user_answer == answer:
            print('정답입니다!')
            time.sleep(1)
            success = True
        else:
            print('틀렸습니다ㅠㅠ')
            time.sleep(1)
            print('정답은', answer, '입니다.')
            time.sleep(1)
            success = False
    except:
        print('숫자와 스페이스바만 입력해 주세요 ^_^')
        user_input = input('정답 >> ')
        answerCheck(user_input, answer)
