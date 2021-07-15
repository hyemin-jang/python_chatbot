import time
import random
import memory
import anagram
import hangman


def miniGame():
    print('공부하느라 지치시죠? 게임 한판 하고 리프레쉬 하세요!', end='\r')
    time.sleep(2)

    playing = 'y'

    while playing == 'y':
        print('*********************** 무엇을 플레이하실래요? ***********************')
        print('1.기억력 테스트   2.용어 복습 게임(oracle)   3.용어 복습 게임(java)   4.나가기')
        choice = input('번호를 입력해주세요 >> ')
        if choice == '1':
            memory.memoryGame()
        elif choice == '2':
            anagram.anagramGame()
        elif choice == '3':
            hangman.hangmanGame()
        elif choice == '4':
            playing = 'n'
            break
        else:
            print('잘못 입력하셨습니다.')
            playing = 'y'
            time.sleep(1)
            continue

        playing = input('다른 게임을 플레이하시겠어요?  y/n >>')

    print('다음에 다시 만나요~')
