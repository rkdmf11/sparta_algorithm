input = 10


# 소수는 자신과 1 외에 아무것도 나눌 수 없음
# 각 숫자를 n이라고 한다면 2~n-1까지 n을 나눌 때까지 나눠떨어지지 않으면 소수
# 주어진 자연수 N이 소수이기 위한 필요충분 조건은
# N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않음
# 수가 수를 나누면 몫이 발생하게 되는데 몫과 나누는 수, 둘 중 하나는 반드시 N의 제곱근 이하이기 때문


def find_prime_list_under_number(number):
    count = 0
    prime_list = []
    for num in range(2, number + 1):
        for i in prime_list:  # 모든 수를 이용하는 것이 아닌, prime_list를 이용해 모든 소수로 나눠 떨어지지 않는지 확인
            if num % i == 0 and i * i <= num:
                break
        else:
            prime_list.append(num)
    return prime_list


result = find_prime_list_under_number(input)
print(result)
