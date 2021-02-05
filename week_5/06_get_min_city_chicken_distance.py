# 여러 개 중 몇개를 골라서 최대한 이득이 되는 경우를 가져와야 된다
# -> 모든 경우의 수를 다 봐야 함 -> "조합" 사용!!!

import itertools, sys

n = 5  # 크기 n*n의 도시
m = 3  # 폐업시키지 않을 치킨집 최대 m개

# 0 = empty, 1 = city, 2 = chicken
city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


def get_min_city_chicken_distance(n, m, city_map):
    chicken_location_list = []
    home_location_list = []

    # 집과 치킨의 위치 저장
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                home_location_list.append([i, j])
            if city_map[i][j] == 2:
                chicken_location_list.append([i, j])

    # print(home_location_list)
    # print(chicken_location_list)

    # 치킨집 중에 M개 고르기(조합)
    # 치킨집의 위치 배열 중 m개씩 뽑을 수 있는 조합 가져와서 chicken_location_m_combinations 에 저장
    # chicken_location_m_combinations = [([1, 2], [2, 2], [4, 4])] <- 튜플 type
    chicken_location_m_combinations = list(itertools.combinations(chicken_location_list, m))
    # print(chicken_location_m_combinations)

    # 최솟값의 초기값을 최대값(sys.maxsize)으로 설정하는 것이 시스템상 좋음
    min_distance_of_m_combinations = sys.maxsize
    # 적은 수이기 때문에 반복문(for)이 3개여도 괜찮다고 함,,
    for chicken_location_m_combination in chicken_location_m_combinations:
        city_chicken_distance = 0
        for home_r, home_c in home_location_list:  # home 의 위치 값 r, c 를 가져 옴
            min_home_chicken_distance = sys.maxsize  # 치킨집과 집의 최소 거리 시스템 최댓값으로 설정 (최소 도시의 치킨 거리)
            for chicken_location in chicken_location_m_combination:  # 각 집의 치킨 거리
                # 치킨집과 집의 최소거리와 각각의 집에서 치킨집과의 거리 중 최소 값 저장
                min_home_chicken_distance = min(min_home_chicken_distance, abs(home_r - chicken_location[0]) + abs(home_c - chicken_location[1]))

            city_chicken_distance += min_home_chicken_distance  # 거리 + 집에서 치킨집까지의 최소 거리(최소 치킨거리)
        min_distance_of_m_combinations = min(min_distance_of_m_combinations, city_chicken_distance)
    return min_distance_of_m_combinations


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!
