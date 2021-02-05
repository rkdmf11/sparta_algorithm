current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#     북  동 남  서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 방향 전환
def get_d_index_when_rotate_to_left(d):
    return (d + 3) % 4

# 후진
def get_d_index_when_go_back(d):
    return (d + 2) % 4


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)
    m = len(room_map[0])
    count_of_departments_cleaned = 1  # 청소하는 칸의 개수
    room_map[r][c] = 2  # 청소 된 부분은 2로 표시
    queue = list([[r, c, d]])

    while queue:  # queue 가 비워지면 종료
        r, c, d = queue.pop(0)  # 첫번째 값 pop
        print(r, c, d)
        temp_d = d  # 현재 방향 저장

        for i in range(4):
            temp_d = get_d_index_when_rotate_to_left(temp_d)  # 현재 방향에서 왼쪽으로 돈 값 -> temp_d는 왼쪽 회전한 값
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]  # 현재 r,c에 현재 방향값 더해줌

            # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면,
            # 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행
            if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0:
                count_of_departments_cleaned += 1
                room_map[new_r][new_c] = 2
                # print(room_map)
                queue.append([new_r, new_c, temp_d])
                break

            # 모든 방향이 청소되어 있다면 뒤로 한 칸 후진
            elif i == 3:  # 갈 곳이 없는 경우
                # 갈 곳이 없으므로 현재 d 값에서 연산
                # 지금 temp_d는 왼쪽으로 회전한 값이므로 사용 X
                new_r, new_c = r + dr[get_d_index_when_go_back(d)], c + dc[get_d_index_when_go_back(d)]
                queue.append([new_r, new_c, d])

                # 네 방향 모두 청소가 이미 되어 있거나 벽이면서 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우 작동을 멈춘다
                # 즉 모든 방향을 봤는데 갈 곳이 없고 뒤도 벽인 경우 멈춤
                if room_map[new_r][new_c] == 1:
                    return count_of_departments_cleaned


# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
