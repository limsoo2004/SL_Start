year = int(input("태어난 년도를 입력하세요: "))

if year % 12 == 8:
    animal = "원숭이"
elif year % 12 == 9:
    animal = "닭"
elif year % 12 == 10:
    animal = "개"
elif year % 12 == 11:
    animal = "돼지"
elif year % 12 == 0:
    animal = "쥐"
elif year % 12 == 1:
    animal = "소"
elif year % 12 == 2:
    animal = "범"
elif year % 12 == 3:
    animal = "토끼"
elif year % 12 == 4:
    animal = "용"
elif year % 12 == 5:
    animal = "뱀"
elif year % 12 == 6:
    animal = "말"
else:
    animal = "양"

print(year, "년의 띠는", animal, "입니다.")
