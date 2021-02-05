numbers = [1, 1, 1, 1, 1]
target_number = 3

result_sum = []  # 경우의 합들
result_count = 0  # target 을 달성할 수 있는 모든 방법의 수를 담기 위한 변수

# 처음 대입되는 값들
# result_sum = target_sum = []
# current_index = 0
# current_sum = 0


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum, target_array):
    if current_index == len(numbers):  # 탈출조건
        target_array.append(current_sum)  # 마지막 인덱스에 다다랐을 때 합계를 추가해줌
        if current_sum == target:  # 타겟과 경우의 연산이 같은 경우 수행
            global result_count  # 외부의 변수를 사용하기 위해 global 사용
            result_count += 1
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1, current_sum + numbers[current_index],
                                                       target_array)
    # 처음 대입 값은 get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, 1, 0 + 1, target_array) 이것을 함수에 대입,
    # 재귀함수이므로 대입을 반복
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1, current_sum - numbers[current_index],
                                                       target_array)


# current_index 와 current_sum 에 0, 0을 넣은 이유는 시작하는 총액이 0, 시작 인덱스도 0이기 때문!
get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0, result_sum)
#print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!
print(result_sum)  # 모든 경우의 수 출력
print(result_count)



"""
파이썬의 Call by Object Reference  라는 개념으로 값이 다르게 나오는 경우가 있음

함수에서 파라미터로 배열을 넘기면 그 내부에 원소를 추가 할 수 있는데
파라미터로 int, str 타입의 변수를 넘기면 그 값이 복제되어 새로운 값을 생성합니다.
(
아래와 같은 경우,,

 numbers = [2, 3, 1]
target_number = 0
result_count = 0  # target 을 달성할 수 있는 모든 방법의 수를 담기 위한 변수


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum, all_ways_count):
    if current_index == len(numbers):  # 탈출조건!
        if current_sum == target:
            all_ways_count += 1  # 마지막 다다랐을 때 합계를 추가해주면 됩니다.
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum + numbers[current_index],
                                                       all_ways_count)
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum - numbers[current_index],
                                                       all_ways_count)


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0, result_count)
# current_index 와 current_sum 에 0, 0을 넣은 이유는 시작하는 총액이 0, 시작 인덱스도 0이니까 그렇습니다!
print(result_count)

 )
따라서 함수 내부의 all_ways_count 만 변경이 되고,
함수 외부의 result_count 는 변하지 않아서 문제가 생깁니다!

이런 경우에는, 함수 외부의 변수를 사용하기 위해 
파이썬의 글로벌 변수라는 걸 사용하시면 됩니다!

외부에 정의되어 있는 변수를 내부에서 사용하기 위해서
global 변수이름 이라고 쓰기만 하면 됩니다! 
"""