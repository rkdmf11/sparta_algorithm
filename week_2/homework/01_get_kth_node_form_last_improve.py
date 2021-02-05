"""
둘다 결국 링크드 리스트의 끝까지 가야 하므로 개선 전과 후는 같은 O(N) 의 성능을 가짐
게다가, 생각해보면 두 개의 공간값을 가지고 이동해야 하므로 비슷하게 연산량을 사용
따라서, 두 번 도는 것보다 한 번 도는 게 무조건 빠르다고는 생각 안하셨으면 좋겠습니다!
"""


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

    def get_kth_node_from_last(self, k):
        fast = self.head
        slow = self.head

        for i in range(k):  # 한 노드를 다른 노드보다 K만큼 떨어지게 함
            fast = fast.next

        while fast is not None:  # 두개의 노드가 같이 빠른 노드가 끝에 도달할때까지 이동
            fast = fast.next
            slow = slow.next  # 느린 노드는 끝에서 k만큰 떨이짐

        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
