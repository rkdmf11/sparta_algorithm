genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    genre_total_play_dic = {}  # genre(key)와 play(value)가 들어있는 dic (중복 key는 value를 합함)
    genre_index_total_play_dic = {}  # genre(key)와 play(value)가 모두 들어있는 dic (인덱스와 play 수가 각각 들어있음)
    for i in range(len(genre_array)):  # genre의 길이만큼 반복하며 위의 딕셔너리에 키와 값을 추가
        genre = genre_array[i]
        play = play_array[i]

        if genre not in genre_total_play_dic:  # 초기값 설정 -> 만약 dic에 저장된 값이 없으면 키와 값 추가
            genre_total_play_dic[genre] = play
            genre_index_total_play_dic[genre] = [[i, play]]
            # [i, play]으로 입력하면 -> {'classic': [0, 500, [2, 150], [3, 800]], 'pop': [1, 600, [4, 2500]]}
        else:  # 추가된 값이 있다면 값(value)에 더해줌
            genre_total_play_dic[genre] += play
            genre_index_total_play_dic[genre].append([i, play])

    print(genre_total_play_dic)  # genre의 총 키와 값의 dic
    print(genre_index_total_play_dic)  # 같은 genre를 기준으로 play 수를 인덱스와 함께 저장한 dic(이때 인덱스는 곡이름이라고 봐도 됨)

    # genre_total_play_dic을 item기준으로 내림차순 정렬
    genre_total_play_dic_sort = sorted(genre_total_play_dic.items(), key=lambda item: item[1], reverse=True)
    print(genre_total_play_dic_sort)

    result = []  # 인덱스들을 저장할 배열

    # genre_total_play_dic_sort를 기준으로 genre_index_total_play_dic을 장르에 따라 정렬
    for genre, value in genre_total_play_dic_sort:
        index_play_array = genre_index_total_play_dic[genre]
        print(index_play_array)
        index_play_array_sort = sorted(index_play_array, key=lambda item: item[1], reverse=True)
        print(index_play_array_sort)

        for i in range(len(index_play_array_sort)):
            if i > 1:
                break
            result.append(index_play_array_sort[i][0])  # index 값만 출력하기 위해 "[0]"을 넣어줌(즉, i번째 [0]번 인덱스 출력)
            # result.append(index_play_array_sort[i])의 경우, [[4, 2500], [1, 600], [3, 800], [0, 500]]출력
    return "결과 = ", result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
