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
    cx_Oracle.init_oracle_client(
        lib_dir=r"C:\playdata\oracle\instantclient_19_11")
    connection = cx_Oracle.connect(
        user='ora01', password='oracle_4U2021', dsn='mydb_high')

    cursor = connection.cursor()

    sql = 'INSERT INTO chatbot(username, jointime, location, gamescore, newskeyword) VALUES (:name, :time, :loca, :score, :search_word)'
    cursor.execute(sql, name=m.name, time=m.now,
                   loca=m.wt.location, score=m.mg.score, search_word=m.ns.search_word)

    connection.commit()
    cursor.close()
    connection.close()
