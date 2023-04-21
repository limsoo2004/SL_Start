'''
작성일 : 2023년 4월 21일
학과 : 컴퓨터공학부
학번 : 202395026
이름 : 임수현
설명 : 잔돈을 구하는 프로그램.
'''

# 넣은 금액 입력
cost = int(input("투입 금액:"))

# 만약 투입금액이 커피값보다 작으면?
if cost < 350:
    print("잔액 부족")
else:
# 커피 가격 뺌
    tleft = cost - 350
# 잔돈 출력
    print("잔돈:",tleft,)
# 500원짜리
if tleft >= 500:
    sum1 = tleft // 500
    left1 = tleft % 500
    print("500원:",sum1,"개")
# 100원짜리
if left1 >= 100:
    sum2 = left1 // 100
    left2 = left1 % 100
    print("100원:",sum2,"개")
# 50원짜리
if left2 >= 50:
    sum3 = left2 // 50
    print("50원:",sum3,"개")

