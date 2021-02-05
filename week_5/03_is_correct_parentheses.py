from collections import deque

balanced_parentheses_string = "()))((()"


def is_correct_parentheses(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:  # s가 ( 이 아니고 stack 이 비어있지 않다면 실행
            stack.pop()
    return len(stack) == 0


def change_to_correct_parentheses(string):
    if string == '':  # 입력이 빈 문자열인 경우, 빈 문자열을 반환
        return ''

    u, v = separate_to_u_v(string)

    if is_correct_parentheses(u):  # 문자열 u가 올바른 괄호 문자열이면 v에 대해 1단계부터 다시 수행
        return u + change_to_correct_parentheses(v)  # 수행한 결과 문자열을 u에 이어 붙인 후 반환
    else:  # 문자열 u가 올바른 괄호 문자열이 아니라면 실행
        # 1. 빈 문자열에 첫 번째 문자로 ( 를 붙임
        # 2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙임
        # 3. ) 를 다시 붙임
        # 4. u의 첫 번째와 마지막 문자 제거하고, 나머지 문자열의 괄호 방향을 뒤집어 뒤에 붙임 -> reverse_parentheses
        # 5. 생성된 문자열 반환
        return '(' + change_to_correct_parentheses(v) + ')' + reverse_parentheses(u[1:-1])


def reverse_parentheses(string):
    reversed_string = ""
    for char in string:
        if char == '(':
            reversed_string += ')'
        else:
            reversed_string += '('
    return reversed_string


def separate_to_u_v(string):  # 균형잡힌 괄호 문자열 u,v 로 분리
    queue = deque(string)
    left, right = 0, 0  # 왼/오 count
    u, v = "", ""  # u = 균형잡힌 괄호 문자열로 더이상 분리 x / v = 빈 문자열이 될 수 있음

    while queue:
        char = queue.popleft()
        u += char  # u는 균형잡힌 괄호 문자열로 더 이상 분리할 수 없어야 한다.
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:  # ( 와 )의 갯수가 같으면 break
            break
    v = ''.join(queue)  # 괄호가 남으면 v에 모두 저장

    return u, v


def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parentheses(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parentheses(balanced_parentheses_string)


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

"""
queue = deque()
    correct_parentheses = []
    open_count = 0
    close_count = 0

    for i in range(len(balanced_parentheses_string) - 1):
        # queue.append(balanced_parentheses_string[i])
        # parentheses = queue.popleft()

        if balanced_parentheses_string[i] == "(":
            correct_parentheses.append(balanced_parentheses_string[i])
            balanced_parentheses_string[i + 1] == ")"
            correct_parentheses.append(balanced_parentheses_string[i+1])
            if balanced_parentheses_string[i + 1] == "(":
                queue.append(balanced_parentheses_string[i + 1])
                open_count += 1

        elif balanced_parentheses_string[i - 1] == ")":
            queue.append(balanced_parentheses_string[i])
            close_count += 1
        print(queue)

    if close_count == open_count:
        for i in range(close_count):
            parentheses = queue.popleft()
            if parentheses == "(":
                correct_parentheses.append("(")
            elif correct_parentheses[-1] == "(":
                correct_parentheses.append(")")

    print(queue)
    print(correct_parentheses)
"""
