input = [4, 6, 2, 9, 1]
# 삽입 정렬은 정렬된 것과 정렬되지 않은 것으로 나뉨
# 먼저, 배열의 [0]번째 인덱스는 다음 인덱스인 [1]의 인덱스를 비교, [0] < [1]라면 pass
# [2]번째 인덱스는 앞의 정렬된 인덱스와 차례대로 비교  -> 이를 반복
# 즉, [1]과 [0]번째 비교, [2]와 [0],[1]번째 비교, [3]과 [0],[1],[2]번째 비교,...


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):  # [0]번째 인덱스는 정렬 되어있는 인덱스이므로 반복 범위에서 제외
        for j in range(i):  # 비교 범위는 한 턴이 돌 수록 증가함으로 i만큼 반복
            if array[i - j - 1] > array[i - j]:  # i = 1, j = 0 -> i-j= 1
                                                       # i = 2, j = 0,1 -> i-j= 2,1
                array[i - j - 1], array[i - j] = array[i - j], array[i - j -1]
            else:
                break  # 비교 수행 시, false인 경우 바로 반복문 break

    return


insertion_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
