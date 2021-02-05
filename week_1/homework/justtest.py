"""input = [3, 16]

def prime(number) :
    for num in range(number[0], number[1]+1):
        for i in num:
            if num % i ==0 :
                break
"""
"""
input = "0001100"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    zero_count = 0
    one_count = 0

    if string[0] == '0':
        one_count += 1
    elif string[0] == '1':
        zero_count += 1
    print(zero_count, one_count)

    for num in range(len(string) - 1):
        if string[num] != string[num + 1]:
            if string[num + 1] == '0':
                one_count += 1
            elif string[num + 1] == '1':
                zero_count += 1

    print(zero_count, one_count)
    return min(zero_count, one_count)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
"""

"""
A, B, C = input()
print(int(A) + int(C))
print(int(A) - int(C))
print(int(A) * int(C))
print(int(A) / int(C))
print(int(A) % int(C))


A, B = map(int, input().split())
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)


a, b, c = map(int, input().split())
print( (a+b)%c, ((a%c) + (b%c))%c, (a*b)%c, ((a%c) * (b%c))%c, sep="\n")



a, b_100, b_10, b = map(int, input().split())
b_sum = a * b
b_10_sum = a * b_10
b_100_sum = a * b_100
sum_multi = b_sum + 10 * b_10_sum + 100 * b_100_sum
print(b_sum)
print(b_10_sum)
print(b_100_sum)
print(sum_multi)
"""
"""
c = 1313
p = c[1]
print(p)
"""

a = int(input())
b = input()
b_sum = a * int(b[2])
b_10_sum = a * int(b[1])
b_100_sum = a * int(b[0])
b_all_sum = b_sum + 10 * b_10_sum + 100 * b_100_sum
print(b_sum, b_10_sum, b_100_sum, b_all_sum, sep="\n")
