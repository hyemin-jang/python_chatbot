import random
import time

question_length = [6, 8, 10]  
answer = []
user_input = []

print('숫자가 나온 순서대로 입력해주세요!')
time.sleep(1.5)
print('(숫자 사이 스페이스바, 완료 후 엔터)')
time.sleep(1.5)

for length in question_length:    
    print('시작!')
    time.sleep(1)
    
    for i in range(length):
        n = random.randrange(0,10)
        answer.append(str(n))
        print(' '*i, n, end='\r')
        
        time.sleep(0.5)
        print(' '*(length+2), end='\r')
        
    try : 
        user_input = input().strip().split(' ')
        
        if answer == user_input:
            print('정답입니다!')
            time.sleep(1)
            if length != question_length[-1]:
                print('다음 단계로 넘어갑니다.')
                time.sleep(1)
        else: 
            print('틀렸습니다ㅠㅠ')
            time.sleep(1)
            break
    except :    
        print('틀렸습니다ㅠㅠ')
        time.sleep(1)
        break
print('게임이 끝났습니다 :)')
