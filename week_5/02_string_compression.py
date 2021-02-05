input = "abcabcabcabcdededededede"


def string_compression(string):
    n = len(string)  # 전체 string 길이 n에 저장
    print(n)
    compression_length_array = []  # 1 ~ len 단위로 압축했을 때 길이 값

    # n의 길이에서 절반 이상의 값은 압축 불가로 절반의 길이까지만 반복
    # 반복 값의 시작으로 0이 아닌 1인 이유는 splited의 renge의 반복 범위 값이 0이면 error 발생,,
    for split_size in range(1, n // 2 + 1):
        # 슬라이싱으로 반복할 값 setting
        # 절반 나눈 값을 반복 범위의 값으로 두고, 슬라이싱은 해당 범위만큼 출력하는,,
        # 전체가 10이고 [0 : 5]이면 인덱스 0부터 4까지 출력
        splited = [string[i: i + split_size] for i in range(0, n, split_size)]
        print("s", splited)  # 슬라이싱 된 값 확인 -> 1개씩 나눈 값, 2개씩 나눈 값, ...

        compressed = ""  # 반복한 문자들 저장해 줄 변수
        count = 1  # 숫자는 자기 자신 포함 해서 카운트 함으로 초기값은 1

        for j in range(1, len(splited)):  # 현재 값과 전의 값을 비교해주기 위해 반복문은 1부터 시작
            prev, cur = splited[j - 1], splited[j]
            if prev == cur:  # 이전 문자와 같다면
                count += 1
            else:  # 이전 문자와 다르다면
                if count > 1:  # 반복 횟수가 1 이상이면
                    compressed += (str(count) + prev)
                else:  # 문자가 반복되지 않고 한번만 나타난 경우로 count 의 초기값인 1은 생략
                    compressed += prev
                count = 1  # 문자 다시 1부터 count 하기 위해 초기화
                # print("c",compressed)

        # for 문에서는 이전값(prev)과 현재값(cur)을 비교 해 이전값을 출력하고 현재 값은 다음 비교 값과 비교
        # 그러므로 마지막의 splited[-1] 이 반복 됐는지를 따로 확인 -> count 확인
        if count > 1:
            compressed += (str(count) + splited[-1])
        else:
            compressed += splited[-1]

        compression_length_array.append(len(compressed))  # compressed 길이 값을 배열에 추가
        print(compressed)  # 압축 된 결과 값 확인
        print(compression_length_array)  # 길이 값 확인

    return min(compression_length_array)


print(string_compression(input))  # 14 가 출력되어야 합니다!
