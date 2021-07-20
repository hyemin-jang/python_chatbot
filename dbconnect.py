# db 연동에 필요한 패키지 import
import pandas as pd
import cx_Oracle

# main import
import main as m

'''
main에 있는 변수 : m.변수명
main에서 import 된 변수 : m.해당파일 별명.해당파일 내 변수명 ex. m.wt.location

수정이 늦어서 정말 죄송해요ㅜ 처음부터 이걸로 했어야했는데
계속 자잘한 오류가 떠서 수정이 늦었습니다..

1. 테이블 열 늘리신 것 확인했습니다.
2. 값을 추가하고 싶으시다면 chatbot 뒤 괄호에 열 이름을 넣고,
3. values 뒤 괄호에 :숫자 추가하신 뒤, 
4. execute문 안에 순서대로 변수 넣어주시면 됩니다!
'''


# db 연동
def db():

    sql = 'INSERT INTO chatbot(username, jointime, location, gamescore, newskeyword) VALUES (:name, :time, :loca, :score, :search_word)'
    m.cursor.execute(sql, name=m.name, time=m.now,
                   loca=m.wt.location, score=m.mg.score, search_word=m.n.search_word)
    
    sql2 = 'INSERT INTO foodlist(username, foodtype, foodname) VALUES (:name, :type, :fname)'
    m.cursor.execute(sql2, name=m.name, type=m.ms.inputed_type, fname=m.ms.inputed_name)

    m.connection.commit()
    m.cursor.close()
    m.connection.close()
