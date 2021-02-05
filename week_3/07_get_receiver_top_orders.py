top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    answer = [0] * len(heights)
    while heights:  # heights가 빈 상자가 되기 전까지 반복
        height = heights.pop()  # 가장 끝에 있는 값을 pop하여 height에 저장
        for idx in range(len(heights) - 1, -1, -1):
            # for문의 범위는 pop이 실행되어 끝의 인덱스가 나간 heights의 길이-1(인덱스는 -1 즉, 3번쩨 인덱스=3-1번째 인덱스이므로)을 시작으로 하고
            # 끝나는 인덱스는 -1 / range의 끝나느 인덱스는 적힌 인덱스 바로 전까지만 loop이므로 0까지 반복하기 위해서 -1 명시
            # range의 3번째 인자는 범위로, -1은 뒤에서 앞으로 하나씩 loop
            if heights[idx] > height:  # heights의 값 중 pop 되었던 마지막 값 보다 큰 수가 있으면
                answer[len(heights)] = idx + 1  # answer에 넣기
                # 범위는 pop되어진 자리에 값을 넣는 것이므로 현재 heights의 길이를 인덱스로 명시, idx+1은 탑의 수를 적어주므로 기존 인덱스의 값+1이 answer에 들어간다.
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
