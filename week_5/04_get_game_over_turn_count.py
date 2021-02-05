k = 4  # 말의 개수

chess_map = [  # 체스판 정보
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [  # 말의 정보-> 행 index, 열 index, 이동 방향
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓  이동 방향은 옆의 화살표 순서대로 0 1 2 3
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


# 동 -> 서 : 0 -> 1
# 서 -> 동 : 1 -> 0
# 북 -> 남 : 2 -> 3
# 남 -> 북 : 3 -> 2

def get_d_index_when_go_back(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    # 말이 쌓일 수 있다고 했으므로 쌓이는 것을 저장해 둬야 하고
    # 현재 맵에 어떻게 말이 쌓일지 저장하기 위해서는 맵을 저장하고 stack 을 이용한다.
    # 즉, current_stacked_horse_map 은 현재 말이 어떻게 쌓인지 저장해 두는 곳
    current_stacked_horse_map = [[[] for _ in range(len(game_map))] for _ in range(len(game_map))]
    # print(current_stacked_horse_map)

    for i in range(horse_count):  # 0~3 번째 말이 어느곳에 있는지 배치
        r, c, d = horse_location_and_directions[i]
        current_stacked_horse_map[r][c].append(i)
    # print(current_stacked_horse_map)

    turn_count = 1
    while turn_count <= 1000:
        for horse_index in range(horse_count):  # horse_index = 현재 이동하는 말의 인덱스
            n = len(game_map)
            r, c, d = horse_location_and_directions[horse_index]
            new_r = r + dr[d]  # 이동방향 d 만큼 움직인 값을 기존의 r에 추가
            new_c = c + dc[d]  # 이동방향 d 만큼 움직인 값을 기존의 c에 추가

            # 파란색 칸인 경우
            # 이동하는 말의 이동방향을 반대로 하고 한 칸 이동
            # 체스판을 벗어나는 경우는 파란색과 같은 경우
            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = get_d_index_when_go_back(d)

                horse_location_and_directions[horse_index][2] = new_d  # 체스 정보의 위치 항목을 새로운 d로 변경
                new_r = r + dr[new_d]
                new_c = c + dc[new_d]

                # 방향을 반대로 변경 후 이동하려는 칸이 파란색인 경우 -> 이동X 가만히 있음
                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue

            moving_horse_index_array = []  # 같이 이동할 말을 저장하기 위한 변수
            for i in range(len(current_stacked_horse_map[r][c])):
                # i = index
                # 즉, [ [[0], [1], [2], []], [[], [], [], []], [[], [], [3], []], [[], [], [], []] ]
                #         ^이부분으로 현재 쌓여져 있는 말의 인덱스 번호..!
                current_stacked_horse_index = current_stacked_horse_map[r][c][i]  # 현재 옮기는 말의 위치(index)
                # 흰색 칸 규칙 -> 이동하려는 칸에 이미 말이 있을 경우
                # 즉, 현재 이동하는 말의 인덱스(horse_index)와 현재 말의 인덱스(i)의 값이 같을 때
                # 이동하는 말을 가장 위에 올려 놓음
                # 이때 이동하는 말은 현재 옮기는 말 위의 말들!
                if horse_index == current_stacked_horse_index:
                    # horse_index 위에 다른 말이 있는 경우 이동하는 말 위의 모든 말이 같이 이동
                    moving_horse_index_array = current_stacked_horse_map[r][c][i:]
                    current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i]  # 이동하는 말의 아래에 있던 말은 그대로 있음
                    break

            # 빨간색 규칙
            # 이동한 후에 이동한 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 변경
            if game_map[new_r][new_c] == 1:
                moving_horse_index_array = reversed(moving_horse_index_array)

            for moving_horse_index in moving_horse_index_array:
                current_stacked_horse_map[new_r][new_c].append(moving_horse_index)
                # horse_location_and_directions 에 이동한 말들의 위치 업데이트
                horse_location_and_directions[moving_horse_index][0], horse_location_and_directions[moving_horse_index][
                    1] = new_r, new_c

            if len(current_stacked_horse_map[new_r][new_c]) >= 4:
                return turn_count
        # print(moving_horse_index_array)

        turn_count += 1
    return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다
