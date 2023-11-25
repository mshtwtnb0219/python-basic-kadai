class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def check_adult(self):
        if self.age >= 20:
            print(f"名前 {self.name} ：年齢{self.age}大人です")
        else:
            print(f"名前 {self.name} ：年齢{self.age}未成年です")

#Humanクラスをインスタンス化してリストに追加
humans = [Human("太郎",10),Human("次郎",20),Human("三郎",15)]

#リストの数分 forを繰り返しcheck_adultを呼び出しする
for human in humans:
    human.check_adult()

