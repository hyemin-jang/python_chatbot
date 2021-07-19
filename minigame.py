import time
import memorygame as mg
import anagramgame as ag
import hangmangame as hg

<<<<<<< HEAD
def miniGame():
    global score
    score = 0

=======

def miniGame():
>>>>>>> fe684152eea89276b997b1bf163364c5913cb44b
    print('공부하느라 지치시죠? 게임 한판 하고 리프레쉬 하세요!', end='\r')
    time.sleep(2)

    playing = 'y'
<<<<<<< HEAD
    
=======

>>>>>>> fe684152eea89276b997b1bf163364c5913cb44b
    while playing == 'y':
        print('*********************** 무엇을 플레이하실래요? ***********************')
        print('1.기억력 테스트   2.용어 복습 게임(oracle)   3.용어 복습 게임(java)   4.나가기')
        choice = input('번호를 입력해주세요 >> ')
        if choice == '1':
            mg.memoryGame()
<<<<<<< HEAD
            score += mg.mg_score
        elif choice == '2':
            ag.anagramGame()
            score += ag.ag_score
        elif choice == '3':
            hg.hangmanGame()
            score += hg.hg_score
        elif choice == '4':
            playing = 'n'
            break      
        else:
            print('잘못 입력하셨습니다.')    
=======
        elif choice == '2':
            ag.anagramGame()
        elif choice == '3':
            hg.hangmanGame()
        elif choice == '4':
            playing = 'n'
            break
        else:
            print('잘못 입력하셨습니다.')
>>>>>>> fe684152eea89276b997b1bf163364c5913cb44b
            playing = 'y'
            time.sleep(1)
            continue

<<<<<<< HEAD
        playing = input('다른 게임을 플레이하시겠어요?  y/n >>').lower() 
        
        while playing not in ['y', 'n']:
            print('잘못 입력하셨습니다.')    
            time.sleep(1)
            playing = input('다른 게임을 플레이하시겠어요?  y/n >>').lower()

    if score != 0:
        print('당신의 게임 총 점수는!!')
        time.sleep(1)
        print(score,'점 입니다 :)')
        time.sleep(1)
    print('다음에 다시 만나요~')


miniGame()

=======
        playing = input('다른 게임을 플레이하시겠어요?  y/n >>')

        while playing not in ['y', 'n']:
            print('잘못 입력하셨습니다.')
            time.sleep(1)
            playing = input('다른 게임을 플레이하시겠어요?  y/n >>')

    print('다음에 다시 만나요~')
>>>>>>> fe684152eea89276b997b1bf163364c5913cb44b
