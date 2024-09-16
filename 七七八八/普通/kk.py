class Record:
    def __init__(self, data, name, id, money):
        self.data = data
        self.name = name
        self.id = id
        self.money = money

    def __str__(self):
        return f"{self.data}, {self.name}, {self.id}, {self.money}"


class filereader:
    def reader(self):
        pass


class filereader1(filereader):
    def __init__(self, path):
        self.path = path

    def read1(self):
        list1 = []
        f = open(self.path, "r", encoding="UTF-8")
        for line in f.readlines():
            line = line.strip()
            line = line.split("，")
            x = Record(line[0], line[1], line[2], line[3])
            list1.append(x)
        f.close()
        return list1


f = filereader1(input("请输入文件路径："))
for x in f.read1():
    print(x)