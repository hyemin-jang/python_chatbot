import time
import random

def anagramGame():
    global ag_score
    ag_score = 0
    words = ['select', 'rollup', 'subquery', 'inner join']
    
    print('\n*********************** oracle 용어 맞추기 게임 ***********************')
    time.sleep(1.5)
    print('수업에서 배운 용어들이 순서가 뒤죽박죽되어 나타납니다.')
    time.sleep(1.5)
    print('무슨 단어인지 입력해주세요!')
    time.sleep(2)

    for word in words:
        makeAnagram(word)
        user_input = input('정답 >> ')
        answerCheck(word, user_input)

        if success == True:
            ag_score += 10
        else:
            break
        if word != words[-1]:
            print('다음 단계로 넘어갑니다.')
            time.sleep(1) 
    
    print('게임이 끝났습니다:)\n( oracle 용어 맞추기 게임 총점수:',ag_score,')')
    time.sleep(2)



def makeAnagram(word):
    word_li = list(word)
    random.shuffle(word_li)
    print(word_li)



def answerCheck(word, user_input):
    global success    

    if user_input.replace(' ','').isalpha(): 
        if user_input == word:            
            print('정답입니다!')
            time.sleep(1)
            success = True        
        else:
            print('틀렸습니다ㅠㅠ')
            time.sleep(1.5)
            print('정답은',word,'입니다.')
            time.sleep(1.5)
            success = False
    else: 
        print('알파벳 단어를 입력해주세요 ^_^')
        user_input = input('정답 >> ')
        answerCheck(word, user_input)


## 추가할사항
# 정답 입력 시간 제한
