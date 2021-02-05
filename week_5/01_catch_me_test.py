from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))  # brown_loc 과 시간을 queue 에 담아줌
    visited = [{} for _ in range(201)]  # 200000의 {} -> brown의 위치(key)와 시간(value)를 담아줌

    while cony_loc <= 200:
        cony_loc += time
        if time in visited[cony_loc]:
            return time

        for i in range(len(queue)):
            current_position, current_time = queue.popleft()

            new_time = current_time + 1

            new_position = current_position - 1
            if 0 <= new_position <= 200 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if 0 <= new_position <= 200 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if 0 <= new_position <= 200 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))



        time += 1
        print(visited)
        print(time)
        print(visited[0])
        print(visited[3])
        print(cony_loc)
        print(visited[cony_loc])
    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!