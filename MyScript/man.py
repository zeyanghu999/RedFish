class Man:
    def __init__(self,name):
        self.name = name #对象的属性之一---“名字”是自己的名字
        print("Initialized!")
    def hello(self):
        print("hello " + self.name + "!")
    def goodbye(self):
        print("Good-bye " + self.name + "!")
m = Man("David")
m.hello()
m.goodbye()
print()
me = Man("1907080207")
me.hello()
me.goodbye()