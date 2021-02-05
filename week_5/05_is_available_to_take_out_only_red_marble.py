from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]
#     북↑ 동→ 남↓ 서←
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# diff = 이동할, game_map은 구멍이 들어가는 부분인지 아닌지 알기 위해
def move_until_wall_or_hole(r, c, diff_r, diff_c, game_map):
    move_count = 0  # 이동한 칸 수
    # 다음 이동이 벽이거나 현재 이동한 곳이 구멍이 아닐 때까지
    while game_map[r + diff_r][c + diff_c] != "#" and game_map[r][c] != "O":
        r += diff_r  # 현재 row 값에 이동한 row 값 즉, diff_r 값 더해줌
        c += diff_c  # 현재 col 값에 이동한 col 값 즉, diff_c 값 더해줌
        move_count += 1  # 이동할 때마다 1 더해줌
    return r, c, move_count


def is_available_to_take_out_only_red_marble(game_map):
    n, m = len(game_map), len(game_map[0])  # 행 수, 열 수
    # visited 안에는 [red_row][red_col][blue_row][blue_col]
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    # print(visited)

    queue = deque()
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1

    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                red_row, red_col = i, j
            elif game_map[i][j] == "B":
                blue_row, blue_col = i, j

    # 최대 10회까지만 탐색 가능
    # red, blue 의 row / col 값과 탐색횟수를 queue에 넣어줌
    # 그리고 visited 에 현재 빨간 구슬, 파란 구슬의 위치를 방문했다고 처리
    queue.append((red_row, red_col, blue_row, blue_col, 1))
    visited[red_row][red_col][blue_row][blue_col] = True

    while queue:
        # 방금 넣었던 red / blue 구슬의 위치 값과 실행 횟수를 변수로 지정
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()
        # 10 이하로 빨간 구슬을 구멍 통해 빼내야 하므로 시도 횟수는 "10회 이하"
        if try_count > 10:
            break

        for i in range(4):  # 4 = 방향(동, 서, 남, 북)
            # 현재 위치를 가지고 현재 어느 방향을 볼 예정인지 -> i 에 의해 방향이 결정
            next_red_row, next_red_col, r_count = move_until_wall_or_hole(red_row, red_col, dr[i], dc[i], game_map)
            next_blue_row, next_blue_col, b_count = move_until_wall_or_hole(blue_row, blue_col, dr[i], dc[i], game_map)

            # 파란 구슬이 구멍에 도착 -> 실패했으니 continue
            if game_map[next_blue_row][next_blue_col] == "O":
                continue
            # 빨간 구슬이 구멍에 도착 -> True
            if game_map[next_red_row][next_red_col] == "O":
                return True

            # 빨간 구슬과 파란 구슬이 동시에 같은 칸에 있을 수 없다.
            if next_red_row == next_blue_row and next_red_col == next_blue_col:
                if r_count > b_count:  # 이동 거리가 많은 구슬을 한칸 뒤로
                    next_red_row -= dr[i]
                    next_red_col -= dc[i]
                else:
                    next_blue_row -= dr[i]
                    next_blue_col -= dc[i]

            # BFS 탐색 마치고 방문 여부 확인해 방문을 안했으면 방문 확인 해주고 queue에 넣어줌
            if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:
                visited[next_red_row][next_red_col][next_blue_row][next_blue_col] = True
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, try_count + 1))
    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다
