import time
def hangmanGame():

    words = ['class', 'instance']

    print('*********************** java 용어 맞추기 게임 ***********************')
    time.sleep(1.5)
    print('당신의 목숨은 3개입니다')
    time.sleep(1.5)
    print('목숨이 사라지기 전에 무슨 단어인지 맞춰주세요!')
    time.sleep(1.5)

    for word in words:
        answer = list(word)
        unknown = ['_' for i in range(len(answer))]
        life = 3

        while unknown.count('_') >= 0 and life >= 0:
            ### while문 종료조건 ###
            if unknown.count('_') == 0:
                print('\n',unknown, ' 남은 목숨:', '♥ '*life)
                print('정답입니다!')
                time.sleep(1.5)
                print('다음 문제로 넘어갑니다.')
                time.sleep(1.5)
                break
            if life == 0:
                time.sleep(1.5)
                print('실패! 남은 목숨이 없습니다ㅠㅠ')
                time.sleep(1.5)    
                print('정답은',word,'입니다.')
                time.sleep(2)
                break        
            
            ### while문 시작 (각 라운드 진행) ###
            print('\n',unknown, ' 남은 목숨:', '♥ '*life)
            user_input = input('알파벳 한 글자씩 추측해보세요 (입력 후 엔터) >> ').lower()

            if user_input.isalpha() and len(user_input)==1 :  
                check = 0 # 맞는 글자가 있는지 
                for i in range(len(answer)):           
                    if answer[i] == user_input:
                        unknown[i] = user_input
                        check += 1
                if check == 0: # 맞는 글자 없으면 목숨 줄어듬
                    life -= 1    
            else :
                print('알파벳 소문자 1글자로 다시 입력해주세요^_^')
                time.sleep(1)

        ### 목숨 없어서 라운드 종료된거면 게임종료 ###
        if life == 0:
            break 
            
    print('게임이 끝났습니다 :)')    


## 추가할 기능:
# 답을 중간에 알았을때 한꺼번에 입력, 점수도 더 많이 주기
# 틀렸을때 답 알려주기
 