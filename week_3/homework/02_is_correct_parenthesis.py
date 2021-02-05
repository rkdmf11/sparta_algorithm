s = "(())()"
"""
예시1. " (())"
1. ( → 괄호가 하나 열렸습니다.   -> ["("]
2. ( → 괄호가 또 하나 열렸네요.  -> ["(", "("]
3. ) → 괄호가 하나 닫혔습니다. 직전 열린괄호랑 같이 나감 -> ["("]
4. ) → 괄호가 하나 닫혔습니다. 직전 직전에 열린 1의 (랑 닫힘 -> []

예시2. "((()"
1. ( → 괄호가 하나 열렸습니다.   -> ["("]
2. ( → 괄호가 또 하나 열렸네요.  -> ["(", "("]
3. ( → 괄호가 또 하나 열렸네요.  -> ["(", "(", "("]
4. ) → 괄호가 하나 닫혔습니다. 직전에 열린 3의 (랑 닫힘  -> ["(", "("]

예시를 통해
1) 닫힌 괄호가 나오면 직전에 열린 괄호가 있는지 봐야 함
2) 열린 괄호들을 다 저장
"""


def is_correct_parenthesis(string):
    stack = []
    for i in range(len(string)):
        if string[i] == "(":  # 열린 괄호라면 stack에 저장
            stack.append(i) # 여기 아무런 값이 들어가도 상관 X! "("가 들어가있는지 여부만 저장해것이기 때문
        elif string[i] == ")":  # 닫힌 괄호라면 직전에 들어온 열린 괄호 즉, 데이터를 pop
            if len(stack) == 0: # 만약 stack에 아무것도 안들어가 있다면 false
                return False    # "))((" 인 경우도 false
            else:
                stack.pop()

    if len(stack) == 0:  # 반복문을 마치고 stack배열에 남아있는 데이터가 없으면 true반환
        return True
    return False  # stack에 데이터가 남아있다면 false


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
