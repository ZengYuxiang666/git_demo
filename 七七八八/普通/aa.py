class record:
    def __init__(self, data, name, id, money):
        self.data = data
        self.name = name
        self.id = id
        self.money = money

    def __str__(self):
        return f"{self.data},{self.name},{self.id},{self.money}"


class read:
    pass


class read1(read):
    def __init__(self, path):
        self.path = path

    def readdata1(self):
        f = open(self.path, "r", encoding="UTF-8")
        my_list = []
        for x in f.readlines():
            x1 = x.strip()
            x2 = x1.split("，")
            y = record(data=x2[0], name=x2[1], id=x2[2], money=x2[3])
            my_list.append(y)
        f.close()
        return my_list


f = read1(path="/销售.txt")
result = f.readdata1()
print(result)