
class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):  # 딕셔너리에는 새로운 key, value를 넣어줘야 함
        index = hash(key) % len(self.items)  # hash(key)로 임의의 문자열로 만들어 배열의 최대 길이만큼 %해줌
        self.items[index] = value


    def get(self, key): # key값에 따른 value값 얻기 위함이므로 인자는 key만 필요
        index = hash(key) % len(self.items)
        return self.items[index]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))