class Human:
    def __init__(self):
        self.name = ""
        self.age = ""
    
    def printinfo(self,name,age):
        self.name = name
        self.age  = age
        print(f"名前{self.name}：年齢{self.age}歳" )

men = Human()
men.printinfo("テスト",23)


