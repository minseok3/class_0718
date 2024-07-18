class 요금:
    def __init__(self,길이,이하요금,이상요금):
        self.a = 길이
        self.b = 이하요금
        self.c = 이상요금
    def 입력문자(self,a):
        result = 0
        if len(a) <= self.a:
            result = self.b
        elif len(a) > self.a:
            result = self.c
        print("요금은:", result)
        return result

요금(20,50,100).입력문자("안녕하세요. 어디가요, 같이가요. 밖에 비와요.")

