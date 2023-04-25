num = int(input("입력할 정수: "))

if num < 0:
    num *= -1

if num < 10:
    print("입력받은 정수는 한 자리수입니다.")
elif num < 100:
    print("입력받은 정수는 두 자리수입니다.")
elif num < 1000:
    print("입력받은 정수는 세 자리수입니다.")
else:
    print("입력받은 정수는 네 자리수 이상입니다")

