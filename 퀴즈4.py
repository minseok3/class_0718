class 회원가입:# 클래스 이름의 첫글자는 대문자
    def __init__(self, 이름, 나이, 연락처):
        self.a = 이름
        self.b = 나이
        self.c = 연락처
    def 정보확인(self):
        print("입력하신 이름은", self.a+"이며, 나이는",self.b+"세 그리고 연락처는",self.c,"입니다.")
var = 회원가입("김민석", "28","010-8366-3459")
var.정보확인()