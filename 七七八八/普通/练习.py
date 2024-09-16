def main1():
    x = input()
    for i in x:
        print(chr(ord(i)+4),end='') # ord()级chr()的作用

def main2():
    c = int(input())
    x = 5*(c-32)/9
    print("c = {:.2f}".format(x))   # 这里不清楚

def main3():
    c = int(input())
    sore = c//10  # 整除，向下取整
    dic = {
        10: 'a',
        9: 'a',
        8: 'b',
        7: 'b',
        6: 'd'
    }
    gread = dic.get(c,"E")   # 与c语言的switch语句相似

def main4():
    while True:
        c = input()
        if int(c) >100000:
            break
        else:
            list = [x for x in c]
            print(len(list))
            for x in list:
                print(x,end=' ')
            print('\n')
            print(c[::-1])

def main5():
    c = int(input("Enter income: "))
    def func(c):
        global total_tax
        if c <= 100000:
            x = c * 0.1
            return x
        elif c > 100000 and c <= 200000:
            x = (c - 100000) * 0.075
            return x + func(100000)
        elif c > 200000 and c <= 400000:
            x = (c - 200000) * 0.05
            return x + func(200000)
        elif c > 400000 and c <= 600000:
            x = (c - 400000) * 0.03
            return x + func(400000)
        elif c > 600000 and c <= 1000000:
            x = (c - 600000) * 0.015
            return x + func(600000)
        else:
            x = (c - 1000000) * 0.001
            return x + func(1000000)

    calculated_tax = func(c)
    print("Total tax: ", calculated_tax)

def main6():
    num1, num2 = map(int,input().split())
    num3 = 0
    if num1 > num2 :
        num3 = num1
        num1 = num2
        num2 = num3
    for x in range(1,num1):
        if num1%(num1-x)==0 and num2%(num1-x) == 0:
            print(f"最大公因数：{num1-x}")
            print(f"最小公倍数：{num1*num2/(num1-x)}")
            break

def main7():
    s = input()
    alpha = 0
    digit = 0
    blank = 0
    other = 0
    for x in s:
        if x.isalpha():
            alpha+=1
        elif x.isdigit():
            digit+=1
        elif x == ' ':
            blank+=1
        else:
            other+=1
    print(f"{alpha } {digit } {blank } {other}")

def main8():
    c = int(input())
    list = [i for i in range(1,c)]
    def func():
        v = 0
        for x in list:
            list.remove(x)
            v+=1
            if v==3:
                list.append(x)
                break
    while len(list)!=1:
        func()
    print(list[0][0])

def main9():
    list = [0,0,0]
    for x in range(3):
        c = input().split()
        list[x] = c
    list.sort()
    for x in list:
        for j in x :
            print(j,end='')
        print()

def main10():
    num1, num2 = map(int, input().split())
    def func1(num1,num2):
        if num1 > num2:
            num3 = 0
            num3 = num1
            num1 = num2
            num2 = num3
        for x in range(1,num1):
            if (num1-x)%num1 == 0 and (num1-x)%num2 == 0:
                return num1-x
    def func2(num1,num2):
        c = func1(num1,num2)
        return num1*num2/c

def main11():
    list = []






