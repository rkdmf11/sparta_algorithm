# Dynamic Programming 기본적 원칙
# 부분 문제 즉, 반복되는 형태로 문제가 계속해서 파생된 것이 있다면 사용
# 메모를 만들어야함

# dynamicProgramming은 Top Down과 Bottom up 방식으로 구현할 수 있다.
# Top Down => Fibo(100) -> Fibo(99) -> Fibo(98) ...
# Bottom up => Fibo(1) -> Fibo(2) -> Fibo(3) ...

input = 100

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo

    return nth_fibo

print(fibo_dynamic_programming(input, memo))