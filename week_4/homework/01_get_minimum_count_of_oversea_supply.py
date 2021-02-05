import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0  # 최소 배송 수를 담을 변수
    current_day_index = 0  # 현재 날짜
    max_heap = []  # 현재 재고 상태에 따라 큰 값을 뽑아 내기 위한 배열

    while stock < k:  # 현재 재고(stock)이 k보다 많게 하는 것이 목표
        for date_index in range(current_day_index, len(dates)):
            if dates[date_index] <= stock:  # dates[i]가 오기 전에 기계가 멈추면 안됨
                heapq.heappush(max_heap, -supplies[date_index])
            else:
                current_day_index = date_index
                break

        answer += 1
        stock += -heapq.heappop(max_heap)

    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))

"""
heap = []
    dic = {}

    while k - stock < 0:
        add = 0
        for i in range(len(dic)):
            add += dic[i]
        print(add)

    for i in range(len(dates)):
        dic[dates[i]] = supplies[i]
    print(dic)
    item = dic.items()
    print(item)

    n = 0
    while n > len(dic):
        heapq.heappush(heap, item(n)(1))
        n += 1
    print(heap)
"""
