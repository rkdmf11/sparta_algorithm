array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]
"""
a [0]
b [0] 비교 -> 작은 것을 배열에 저장 
a[] b[]와 비교 시 a가 작을 경우, b가 작을 경우의 식
a는 if i < j의 조건식으로 append, b는 다른 조건식,, 
"""


def merge(array1, array2):
    array_c = []
    array1_index = 0
    array2_index = 0

    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            array_c.append(array1[array1_index])
            array1_index += 1
        else:
            array_c.append(array2[array2_index])
            array2_index += 1

        if array1_index == len(array1):
            while array2_index < len(array2):
                array_c.append(array2[array2_index])
                array2_index += 1
        if array2_index == len(array2):
            while array1_index < len(array1):
                array_c.append(array1[array1_index])
                array1_index += 1

    return array_c


"""
    for i in array1:
        for j in array2:
            if i < j:
                marge_array.append(i)
                break
            if i > j:
                marge_array.append(j)

            print(marge_array)
            """

print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!
