# MaxHeep은 최소값이나 최댓값을 빨리 뽑아야 할 때 사용 (다른 배열들은 어떻게 배열되어 있든지 상관 x)


class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        delete_node = self.items.pop()
        cur_index = 1
        print(cur_index)

        while cur_index <= len(self.items) - 1:
            left_index = cur_index * 2
            right_index = cur_index * 2 + 1
            max_index = cur_index
            print("cur : ", cur_index, 'max : ', max_index, "left : ", left_index, "right : ", right_index)
            if left_index <= len(self.items) - 1 and self.items[left_index] > self.items[max_index]:
                max_index = left_index
            if right_index <= len(self.items) - 1 and self.items[right_index] > self.items[max_index]:
                max_index = right_index
            if max_index == cur_index:
                break

            print("cur2 : ", cur_index, 'max2 : ', max_index, "left2 : ", left_index, "right2 : ", right_index)
            self.items[max_index], self.items[cur_index] = self.items[cur_index], self.items[max_index]  # 위에서 비교한 것을 교체
            cur_index = max_index

        return delete_node  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(7)
max_heap.insert(6)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 7, 6, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 5, 6, 2, 4]

"""
    def delete(self):
        cur_index = len(self.items) - 1
        self.items[1], self.items[cur_index] = self.items[cur_index], self.items[1]
        delete_node = self.items.pop()
        cur_index = 1
        print(cur_index)

        while cur_index <= len(self.items) - 1:
            left_index = cur_index * 2
            right_index = cur_index * 2 + 1
            print("cur : ", cur_index, "left : ", left_index, "right : ", right_index)
            if self.items[left_index] > self.items[right_index]:
                self.items[left_index], self.items[cur_index] = self.items[cur_index], self.items[left_index]
                cur_index = left_index
            elif self.items[left_index] < self.items[right_index]:
                self.items[right_index], self.items[cur_index] = self.items[cur_index], self.items[right_index]
                cur_index = right_index
            else:
                break
        return delete_node  # 8 을 반환해야 합니다.
"""
