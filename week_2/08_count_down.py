# 아래와 같이 재귀함수는 자기가 자신을 부르고 있는 구조
# 즉 반복해서 자신을 호출한다는 의미
# 재귀함수는 무한정 돌게하면 안됨 즉, 언제 끝나는지 탈출조건 알려줘야 함
# 탈출조건 제시 안할 시, RecursinError 발생
# 재귀함수는 자기자신을 호출함으로서 코드를 간결하고 명확하게 만들 수 있는 장점 존재

def count_down(number):
    if number < 0:
        return
    print(number)          # number를 출력하고
    count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!


count_down(60)