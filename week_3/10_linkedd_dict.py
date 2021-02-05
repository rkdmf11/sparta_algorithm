# 해쉬 테이블은 파이썬의 딕셔너리와 같은 개념!

class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v

class LinkedDict: # 충돌 대비 class
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def add(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)

    def get(self, key):
        index = hash(key) % len(self.items)
        print("인덱스", index)
        return self.items[index].get(key)



link = LinkedDict()
link.add("test", 3)
print(link.get("test"))

link.add("fast", "빠른")
print(link.get("fast"))
link.add("slow", "느린")
print(link.get("slow"))
link.add("test1", 7)
print(link.get("test1"))
link.add("just", "Boom")
print(link.get("just"))