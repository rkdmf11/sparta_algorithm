input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array)
    for i in range(n - 1): # i = 반복 횟수, j = 인덱스
        for j in range(n - i - 1): # 반복 횟수에서 1은 두개씩 비교 함이고 i는 반복 횟수의 범위가 감소함임
            if array[j] > array[j + 1]:
                #print(array[j], array[j + 1])
                array[j], array[j + 1] = array[j + 1], array[j]
                #print(array[j], array[j + 1])
    return


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!