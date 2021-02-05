class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        # " -1 "이라는 코드가 있으면 0은 어떻게 될까라는 고민을 해야 함
        # 때문에 위와 같은 조건문(if) 넣어 줌
        node = self.get_node(index - 1)  # class 내의 함수 호출
        next_node = node.next
        node.next = new_node
        new_node.next = next_node
        print(node.data, next_node.data, node.next.data, new_node.next.data)


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(7)
linked_list.append(3)
print(linked_list.get_node(0).data)  # -> 5를 들고 있는 노드를 반환해야 합니다!
print(linked_list.get_node(1).data)
linked_list.print_all()
linked_list.add_node(2, 17)
linked_list.print_all()
