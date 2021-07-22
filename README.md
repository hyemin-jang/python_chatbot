# 플레e봇(파이썬 챗봇)

## 💡 기획의도
플레이 데이터에서 열심히 수강하고 있는 학생들을 위해 주로 사용하 는 기능들을 모은 챗봇입니다. 
플레이 데이터 과목, 남은 수강 일자부터 매일매일 필요한 점심 메뉴, 날씨, 코로나 정보, 뉴스 정보, 그리고 쉬어갈 수 있는 게임까지 없는 거 빼고 다 있는 챗봇이니, 자주 이용해 주세요!

## 📄 서비스 구성도
<img width="398" alt="서비스 구성도" src="https://user-images.githubusercontent.com/68639271/126582999-2f8d17c8-c728-48fa-8218-a0fdf19e99c6.png">

- 서비스 전체 실행(test.py), 챗봇 기능 실행(main.py), 데이터베이스 연동(dbconnect.py)
- 입실/퇴실 알림(alarm.py)
- 날씨 정보(weather.py)
- 플레이데이터 시간표(schedule_check.py, print_schedule.py, CONST.py)
- 점심메뉴 고르기(menuselect.py)
- 미니게임(minigame.py, memorygame.py, anagramgame.py, hangmangame.py)
- 코로나 확진 현황(corona.py)
- 오늘의 뉴스 정보(news.py)
- 플레이 유저 정보 조회(check_db_info.py)

## 👨‍👨‍👧 구성원
- 민경준(팀장) : 플레이데이터 시간표, 플레이 유저 정보 조회 [Cameron Min Github](https://github.com/keyongjun)
- 장혜민 : 미니게임 3종 [hyemin-jang Github](https://github.com/hyemin-jang)
- 박서은 : 입실/퇴실 알림, 오늘의 뉴스 정보 [westsi1ver Github](https://github.com/westsi1ver)
- 박세은 : 점심메뉴 고르기 [sennyS2 Github](https://github.com/seeun214)
- 배지수 : 날씨 정보, 코로나 확진 현황, 챗봇 기능 실행 [geesuee Github](https://github.com/geesuee)
