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


def get_linked_list_sum(linked_list_1, linked_list_2):
    sum_1 = _get_linked_list_sum(linked_list_1)
    sum_2 = _get_linked_list_sum(linked_list_2)
    """
    sum_1과 sum_2의 코드가 중복됨 -> 중복 부분을 줄임
    
    sum_1 = 0
    head_1 = linked_list_1.head
    while head_1 is not None:
        sum_1 += sum_1 * 10 + head_1.data
        head_1 = head_1.next

    sum_2 = 0
    head_2 = linked_list_2.head
    while head_2 is not None:
        sum_2 += sum_2 * 10 + head_1.data
        head_2 = head_2.next

    print(sum_1)
    print(sum_2)

    """

    return sum_1 + sum_2


def _get_linked_list_sum(linked_list):
    # 이미 정의되어있는 함수는 사용하지 말자 (sum(x) -> linked_list_sum(o))
    linked_list_sum = 0
    head = linked_list.head
    while head is not None:
        linked_list_sum = linked_list_sum * 10 + head.data
        head = head.next
        print(linked_list_sum) # 그냥 확인차,,
    return linked_list_sum


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))