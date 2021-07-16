import time
import print_schedule as schedule


def schedule_check():
    print("오늘 배울 공부 시간표와 선행학습할 내용을 확인할 수 있습니다. 어떤 것을 선택하시겠습니까?")
    print("===================================================================================")

    while True:
        time.sleep(2)
        option = input("1. 오늘 학습할 내용   2. 해당 날짜 학습할 내용   3. 나가기 : ")
        if option == '1':
            schedule.print_schedule()
        elif option == '2':
            schedule.study_in_advance()
        elif option == '3':
            time.sleep(1)
            print("이용해주셔서 감사합니다. ")
            break
        else:
            time.sleep(1)
            print('잘못된 입력 값입니다.')
            continue
