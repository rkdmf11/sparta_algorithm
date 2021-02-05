# 문제가 반복되고, 반복되는 구조 속에서 해결되는 구조가 있으면 재귀함수로 풀면 됨
# 재귀함수 사용시, 탈출방법 필수 명시!

input = "소주만병만주소"


def is_palindrome(string):
    print(string)
    if string[0] != string[-1]:
        return False
    if len(string) <= 1:
        return True
    return is_palindrome(string[1:-1])


print(is_palindrome(input))