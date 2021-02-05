input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n = len(array)
    for i in range(n - 1): # 반복의 첫번째 자리 인덱스
        min_index = i # 최소값을 담을 변수
        for j in range(n - i): # 비교할 수 반복
            if array[i + j] < array[min_index]: # 비교 후 가장 작은 수를 인덱스의 앞으로 정렬 반복
                min_index = i + j
                #print(min_index)
            array[i], array[min_index] = array[min_index], array[i]
            # 첫번째 인덱스와 첫회전 후 나온 가장 작은 수의 인덱스의 위치를 변경
    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!