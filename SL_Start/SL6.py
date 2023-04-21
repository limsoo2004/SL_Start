yr = int(input("연도:"))

if (yr % 4 == 0 and yr % 100 != 0) or yr % 400 == 0:
    print("윤년")
else :
    print("윤년 아님")