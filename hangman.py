import time
def hangmanGame():

    words = {'class' : '설계도' ,
             'instance' : '메모리에 생성된 실체', 
             'overriding' : '메소드 OOOOO'}

    print('\n*********************** java 용어 맞추기 게임 ***********************')
    time.sleep(1.5)
    print('목숨이 사라지기 전에 무슨 단어인지 맞춰주세요!')
    time.sleep(1.5)
    print('알파벳 한 글자씩 추측해보세요. 답을 눈치챘다면 정답 바로 입력!')
    time.sleep(1.5)

    round = 0
    for word in words:
        word_li = list(word)
        unknown = ['_' for i in range(len(word_li))]
        life = (len(word) // 2) + 1

        ### 각 라운드 진행 ###
        while unknown.count('_') >= 0 and life >= 0:
            
            ### while문 종료조건 1 : 정답 맞췄을때 ###
            if unknown.count('_') == 0:                
                print('정답입니다!')
                time.sleep(1.5)
                # 마지막 라운드가 아닐때만
                if round < len(words):
                    print('다음 문제로 넘어갑니다.')
                    time.sleep(1.5)
                break
            ### while문 종료조건 2 : 목숨 다잃었을때 ###    
            if life == 0:
                print('실패! 남은 목숨이 없습니다ㅠㅠ')
                time.sleep(1.5)    
                print('정답은',word,'입니다.')
                time.sleep(2)
                break        
            
            print('\n남은 목숨:', '♥ '*life)
            print(unknown, ' 힌트:', words[word])           
                
            user_input = input('>> ').lower()

            if user_input.isalpha() and len(user_input)==1 :  
                if user_input in unknown:
                    print('이미 입력한 글자입니다.')
                    time.sleep(1)
                    continue
                ### 맞춘 글자가 있는지 체크 ###
                check = 0 
                for i in range(len(word_li)):           
                    if word_li[i] == user_input:
                        unknown[i] = user_input
                        check += 1
                if check == 0: # 맞는 글자 없으면 목숨 줄어듬
                    life -= 1     
                                   
            elif user_input == word :
                unknown = []       
            else :
                print('알파벳 소문자 1글자로 다시 입력해주세요^_^')
                time.sleep(1)

            round += 1

        ### 목숨 없어서 라운드 종료된거면 게임종료 ###
        if life == 0:
            break 
            
    print('게임이 끝났습니다 :)')    

