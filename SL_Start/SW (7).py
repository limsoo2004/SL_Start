id = input("아이디를 입력하세요: ")
pw = input("패스워드를 입력하세요: ")

if id == "admin" and pw == "pw1234":
    print("로그인 성공")
elif id != "admin":
    print("아이디가 틀렸습니다.")
else:
    print("패스워드가 틀렸습니다.")
