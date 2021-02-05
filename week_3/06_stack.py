class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:  # stack은 삽입/삭제가 빈번!
    def __init__(self):
        self.head = None  # stack도 head를 통해서 넣고 빼는 작업을 수행하기 때문에 head를 저장

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    # pop 기능 구현
    def pop(self):  # pop이란는 함수를 사용하면 가장 위에서 뽑았던 데이터를 반환해줘야 함
        if self.is_empty():  # 메소드 사용 시, self 붙이기
            return "Stack is Empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head.data

    def peek(self):  # 가장 위에 있는 것을 반환해주기만 하면 됨
        return self.head.data

    # is_Empty 기능 구현
    def is_empty(self):  # empty이면 True, 아니면 False
        return self.head is None


stack = Stack()
stack.push(3)
print(stack.peek())
stack.push(5)
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.is_empty())

stack.push(7)
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.is_empty())
