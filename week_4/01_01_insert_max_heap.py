class MaxHeap:
    def __init__(self):
        self.items = [None]  # 완전이진트리를 배열로 저장하기 위해서는 none값을 [0]번째에 저장
                             # 부모 노드를 찾기 위해서는 "자식노드//2"

    def insert(self, value):
        self.items.append(value)  # 배열로 관리하고 있으므로 노드로 만들지 않고 value를 넣어줌
        cur_index = len(self.items) - 1  # 마지막 인덱스
        print("초기 설정 : ", cur_index)

        while cur_index > 1:  # 마지막 인덱스(추가된 인덱스)가 부모 노드가 될 때까지
            parent_node = cur_index // 2
            print("first : ", cur_index, parent_node)
            if self.items[cur_index] > self.items[parent_node]:
                self.items[cur_index], self.items[parent_node] = self.items[parent_node], self.items[cur_index]
                cur_index = parent_node  # 비교 해서 부모 인덱스를 새로 들어온 인덱스와 값을 변경 -> 탈출문을 빠져나오거나 큰 수가 들어올때 최상위 노드로 옮기기 위함
                print("second : ", cur_index, parent_node)
            else:
                break
        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!