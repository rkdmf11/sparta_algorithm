input = "011110"


# 이 알고리즘에서 포인트
# 1) 뒤집어 질 경우
# 2) 첫 번째 원소가 0인지 1인지


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_one = 0
    count_zero = 0
    if string[0] == '0':  # 첫번째 자리 확인 한 후 count
        count_one += 1
    elif string[0] == '1':
        count_zero += 1
    print(count_one, count_zero)

    for i in range(len(string) - 1):  # i와 i+1을 비교함으로 string-1만큼의 길이만 반복
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':  # i+1부터 0인지 1인지 판단 후 count -> 첫번째자리는 확인X
                count_one += 1
            if string[i + 1] == '1':
                count_zero += 1
    print(count_one, count_zero)
    return min(count_one, count_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
