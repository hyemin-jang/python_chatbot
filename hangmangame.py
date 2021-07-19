import time

hg_score = 0
words = {'class' : '설계도' ,
            'instance' : 'A a = new A()', 
            'overriding' : '메소드 OOOOO'}



def hangmanGame():
    global life, unknown, user_input, checked_letter, hg_score
    
    print('\n*********************** java 용어 맞추기 게임 ***********************')
    time.sleep(1.5)
    print('목숨이 사라지기 전에 무슨 단어인지 맞춰주세요!')
    time.sleep(1.5)
    print('알파벳 한 글자씩 추측해보세요. 답을 눈치챘다면 정답 바로 입력!')
    time.sleep(1.5)

    round = 0
    for word in words:
        life = (len(word) // 2) + 1
        unknown = ['_' for i in range(len(word))]
        checked_letter = []
        
        # 성공 혹은 실패할때까지 글자추측 반복
        while unknown.count('_') > 0 and life > 0: 
            print('\n남은 목숨:', '♥ '*life)
            print(unknown, ' 힌트:', words[word])        
            user_input = input('>> ')            
            
            validCheck(word)       
            letterCheck(word)  

        # 성공/실패 여부 확인    
        successCheck(word) 
        round += 1

        if success == True:
            hg_score += 10
        else:
            break
        if round < len(words):
            print('다음 단계로 넘어갑니다.')
            time.sleep(1)        
            
    print('게임이 끝났습니다:)\n( java 용어 맞추기 게임 총점수:',hg_score,')')
    time.sleep(2)


def validCheck(word):     
    global user_input, unknown, checked_letter
    
    if user_input.isalpha() and len(user_input) == 1 :           
        if user_input in checked_letter:                            
            print('이미 입력한 글자입니다.')
            time.sleep(1)
            user_input = input('>> ')
            validCheck(word)               
    else: 
        if user_input != word:
            print('알파벳 소문자 1글자로 다시 입력해주세요^_^')
            time.sleep(1) 
            user_input = input('>> ')
            validCheck(word)          
    checked_letter.append(user_input)
                               
    

def letterCheck(word):
    global life, unknown, user_input
    
    if word == user_input:
        unknown = [] # 바로 성공
    else:
        check = 0
        for i in range(len(word)):           
            if word[i] == user_input:
                unknown[i] = user_input                
                check += 1   
        if check == 0: 
            life -= 1         


def successCheck(word):
    global success, life, unknown
        
    if unknown.count('_') == 0:                
        print('정답입니다!')
        time.sleep(1.5)
        success = True
    elif life == 0:
        print('실패! 남은 목숨이 없습니다ㅠㅠ')
        time.sleep(1.5)    
        print('정답은',word,'입니다.')
        time.sleep(2)
        success = False     
    
        
