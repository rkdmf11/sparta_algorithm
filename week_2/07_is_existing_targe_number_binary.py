finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]
# 이진탐색을 하기 위해서는 항상 일정한 규칙으로 정렬되어 있는 데이터 일때만 가능
# 즉 위와 같은 불규칙한 배열에서는 이진탐색은 불가..!


def is_exist_target_number_binary(target, numbers):
    for num in numbers:
        if num == target:
            return True
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)
