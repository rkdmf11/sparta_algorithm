class Person:
    def __init__(self, param_name):
        print("i am created! ", self)  # self=인자에 자기 자신을 넘겨줌
        self.name = param_name

    def talk(self):  # class내부 함수를 메소드를 함 즉, talk메소드를 만들었다
        print("안녕하세요, 제 이름은 ", self.name, "입니다.")


person_1 = Person("유재석")  # () <- 생성자로, 객체를 생성할 때 쓰는 함수
print(person_1.name)
person_1.talk()
print(person_1)
person_2 = Person("박명수")
person_2.talk()
print(person_2)
