# class 캐릭터:# 클래스 이름의 첫글자는 대문자
#     def __init__(self, id, sex, job):
#         self.Character_id = id
#         self.Character_sex = sex
#         self.Character_job = job
#     def attak(self):
#         print(self.Character_id +" "+"공격"+"!"*10)
#
# min = 캐릭터("민석","남","전사")
# min.attak()

class 캐릭터:# 클래스 이름의 첫글자는 대문자
    def __init__(self, id, sex, job):
        self.Character_id = id
        self.Character_sex = sex
        self.Character_job = job
    def attak(self, 상대방_id):
        print(self.Character_id , 상대방_id +"공격"+"!"*10)

min = 캐릭터("민석","남","전사")
min.attak("파이리")