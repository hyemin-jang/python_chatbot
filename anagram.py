import time
import random

def anagramGame():

    words = ['subquery', 'grouping', 'inner join']
    
    print('\n*********************** oracle 용어 맞추기 게임 ***********************')
    time.sleep(1.5)
    print('수업에서 배운 용어들이 순서가 뒤죽박죽되어 나타납니다.')
    time.sleep(1.5)
    print('무슨 단어인지 입력해주세요!')
    time.sleep(2)

    round = 0
    ### 각 라운드 진행 ###
    while round < len(words):
        print('시작!')
        time.sleep(1.5)         
        word_li = list(words[round])
        random.shuffle(word_li)
        print(word_li)
        
        user_input = input('정답 >> ')
        if user_input.isalpha():
            if user_input == words[round]:            
                print('정답입니다!')
                time.sleep(1)
                if words[round] != words[-1]:  #마지막 라운드일경우 print 안하고 게임종료
                    print('다음 단계로 넘어갑니다.')
                    round += 1
                    time.sleep(1)            
            else:
                print('틀렸습니다ㅠㅠ')
                time.sleep(1.5)
                print('정답은',words[round],'입니다.')
                time.sleep(1.5)
                round += 1
                break
        
        # 잘못 입력하면 다음 round로 돌아가지 않고 문제 다시 출력
        else: 
            print('알파벳 단어를 입력해주세요 ^_^')
            time.sleep(1)

    print('게임이 끝났습니다 :)')  

## 추가할사항
# 정답 입력 시간 제한