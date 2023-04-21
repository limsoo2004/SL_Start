'''
작성일 : 2023년 4월 21일
학과 : 컴퓨터공학부
학번 : 202395026
이름 : 임수현
설명 : 입장료를 구하는 프로그램.
'''

# 어린이, 성인, 노인 수 입력받음
kid = int(input("어린이:"))
man = int(input("성인:"))
old = int(input("노인:"))

# 총 인원 구하기
count = kid + man + old

# 총 금액 구하기
total = kid * 5000 + man * 10000 + old * 7000

# 만약 인원 수가 10명이 넘어가면 
if count >= 10:
# 20% dc해줌
    disc = total / 100 * 80
    print("할인 받은 총 금액:",disc,)
# 아님 말고
else:
    print("총 금액:",total,)