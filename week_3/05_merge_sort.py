array = [5, 3, 2, 1, 6, 8, 7, 4]

# 1단계 [1, 2, 3, 5] [4, 6 ,7 ,8] 길이 N/2 2개 비교하면서 합친다 => N/2 * 2 = N의 시간복잡도
# 2단계 [3, 5] [1, 2] -> [1, 2, 3, 5] 길이 N/4 2개 비교    길이 N을 반으로 2번 쪼개서 N/4이고 4개 비교하여 아래와 같은 식 도출
#      [6, 8] [4, 7] -> [4, 6, 7, 8] 길이 N/4 2개 비교 =>  N/4 * 4 = N의 시간복잡도
# k단계 [6] [8]
# n/2^k = 1 -> k = log2N
# 즉, k단계만큼 반복하는데 각각 단계는 O(N) 시간복잡도를 가진다
# 즉, log2N * O(N) -> O(NlogN)


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])
    print(array)
    print('left_array', left_array)
    print('right_array', right_array)
    return merge(left_array, right_array)


def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        # 이때 최대로 사용될 수 있는 시간 복잡도는 array1과 array2의 길이 -> len(array1)+len(array2)
        # 즉, array1과 array2는 array를 반으로 쪼갠것과 같아
        # (why?위의 marge_sort함수로 array가 반으로 쪼개져 mmerge함수에 대입되기 때문)
        # O(N)만큼의 시간복잡도 가지고 있음
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!
