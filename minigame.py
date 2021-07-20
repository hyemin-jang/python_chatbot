import time
import memorygame 
import anagramgame 
import hangmangame 

score = None

def miniGame():    
    global score 
    score = 0
    print('공부하느라 지치시죠? 게임 한판 하고 리프레쉬 하세요!', end='\r')
    time.sleep(2)
    
    playing = 'y'    
    while playing == 'y':
        message= ' 무엇을 플레이하실래요? '
        print('='*((100-len(message))//2) + message + '='*((100-len(message))//2))
        print('1.기억력 테스트   2.용어 복습 게임(oracle)   3.용어 복습 게임(java)   4.나가기')
        choice = input('번호를 입력해주세요 >> ')
        if choice == '1':
            memorygame.memoryGame()
            score += memorygame.mg_score
        elif choice == '2':
            anagramgame.anagramGame()
            score += anagramgame.ag_score
        elif choice == '3':
            hangmangame.hangmanGame()
            score += hangmangame.hg_score
        elif choice == '4':
            playing = 'n'
            break      
        else:
            print('잘못 입력하셨습니다.')    
            playing = 'y'
            time.sleep(1)
            continue

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




