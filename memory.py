import random
import time

def memoryGame():

    num_length = [6, 8, 10]   # 각 라운드별 나오는 숫자 개수
    
    print('\n*********************** 기억력 테스트 게임 ***********************')
    time.sleep(1.5)
    print('숫자가 나온 순서대로 입력해주세요!')
    time.sleep(1.5)
    print('(숫자 사이 스페이스바, 완료 후 엔터)')
    time.sleep(2)

    ### 나오는 숫자 개수 다르게 해서 3라운드 진행 ###
    for length in num_length:  
        answer = [] 
        user_input = []
        print('시작!')
        time.sleep(2)
        
    ### 각 라운드 시작 ###
        # legth 길이만큼 숫자출력
        for i in range(length):
            n = random.randrange(0,10)
            answer.append(n)    
            print(' '*i, n, end='\r')  # 숫자 가로로 이동하며 출력
            time.sleep(0.5)
            print(' '*(length+2), end='\r')

        # 유저 정답 받아서 확인  
        while 1:                    
            try: 
                user_input = list(map(int, input('정답 >> ').strip().split(' ')))
                if user_input == answer:
                    print('정답입니다!')
                    time.sleep(1)
                    # 마지막 라운드 아니면 print출력, 마지막 라운드면 종료
                    if length != num_length[-1]:
                        print('다음 단계로 넘어갑니다.')
                        time.sleep(1)  
                    else:
                        break
                else: 
                    print('틀렸습니다ㅠㅠ')
                    time.sleep(1)
                    print('정답은', answer, '입니다.')
                    break
            except:
                print('숫자와 스페이스바만 입력해 주세요 ^_^')                
        
    print('게임이 끝났습니다 :)')


