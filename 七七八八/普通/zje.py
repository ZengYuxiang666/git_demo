class students :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name},{self.age}"
student1=students("zyx",18)
print(student1)

class phone :
    __is_5g_enable =False
    def __cheak_5g(self):
        if self.__is_5g_enable == True:
            print("5g开启")
        else :
            print("5g关闭,使用4g")
    def call_by_5g(self):
        self.__cheak_5g()
        print("正在通话中")
phone1 = phone()
phone1.call_by_5g()
from typing import Union

def add(x,y) ->Union[int,str] :
    return x + y
add(9,9)
