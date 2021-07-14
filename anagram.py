import time
import random

def anagramGame():

    words = ['select', 'subquery', 'inner join']

    print('수업에서 배운 용어들이 순서가 뒤죽박죽되어 나타납니다.')
    time.sleep(1.5)
    print('무슨 단어인지 입력해주세요!')
    time.sleep(1.5)

    for word in words:
        print('시작!')
        time.sleep(1.5)
        word_li = list(word)
        random.shuffle(word_li)
        print(''.join(word_li))
        time.sleep(1)
        

        if input() == word:
            print('정답입니다!')
            time.sleep(1)
            print('다음 문제로 넘어갑니다.')
            time.sleep(1.5)
        else:
            print('틀렸습니다ㅠㅠ')
            time.sleep(1.5)
            break

    print('게임이 끝났습니다 :)')  



if __name__ == "__main__":
    anagramGame()
