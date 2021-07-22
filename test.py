class Animal:
    __COUNT=5 # 私有属性全部被替换
    __AGE=9
    def __init__(self,name):
        self.__AGE+=1
        self._name=name
        self.__COUNT+=2

class Hipo(Animal):
    __COUNT=55
    __AGE=88
    _Animal__AGE=99 # 此属性才真正替换了父类的__AGE属性
    def __init__(self,name):
        super().__init__(name)
        self.__AGE+=1
        self.__COUNT+=2

h=Hipo('hipo')
print(h.__dict__)
print(Hipo.__dict__)
print(Animal.__dict__)