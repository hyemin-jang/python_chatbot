# 플레e봇(파이썬 챗봇)

## 💡 기획의도
플레이데이터에서 열심히 수강하고 있는 학생들이 편리하게 사용할 만한 기능들을 모은 봇입니다. 
과목 조회, 남은 수강 일자 조회, 매일매일 필요한 점심 메뉴, 날씨, 코로나 정보, 뉴스 정보, 그리고 쉬어갈 수 있는 게임까지 없는 거 빼고 다 있는 챗봇이니, 자주 이용해 주세요!

## 📄 서비스 구성도
<img width="398" alt="서비스 구성도" src="https://user-images.githubusercontent.com/68639271/126582999-2f8d17c8-c728-48fa-8218-a0fdf19e99c6.png">

- 서비스 전체 실행(test.py), 챗봇 기능 실행(main.py), 데이터베이스 연동(dbconnect.py)
- 입실/퇴실 알림(alarm.py)
- 날씨 정보(weather.py)
- 플레이데이터 시간표(schedule_check.py)
- 점심메뉴 고르기(menuselect.py)
- 미니게임(minigame.py)
- 코로나 확진 현황(corona.py)
- 오늘의 뉴스 정보(news.py)
- 플레이 유저 정보 조회(check_db_info.py)

## 🎮 Technical Report 및 실행파일
https://drive.google.com/drive/folders/1yjIpyjpNAMGRlD5-iXID92mkpZov813r?usp=sharing
- '플레e봇(1.2)_cloud.zip' 다운로드 및 압축 해제
- '[플레e봇]실행 전 읽기' 텍스트 파일 안내에 따라 플레e봇.exe 실행


## 👨‍👨‍👧 구성원
- 민경준 : 플레이데이터 시간표, 플레이 유저 정보 조회 [Cameron Min Github](https://github.com/keyongjun)
- 장혜민 : 미니게임 3종 [hyemin-jang Github](https://github.com/hyemin-jang)
- 박서은 : 입실/퇴실 알림, 오늘의 뉴스 정보 [westsi1ver Github](https://github.com/westsi1ver)
- 박세은 : 점심메뉴 고르기 [sennyS2 Github](https://github.com/seeun214)
- 배지수 : 날씨 정보, 코로나 확진 현황, 챗봇 기능 실행 [geesuee Github](https://github.com/geesuee) / [velog 파이썬 챗봇 시리즈](https://velog.io/@geesuee/series/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%B1%97%EB%B4%87)
