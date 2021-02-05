# 최대로 할인하면 총 내야 될 금액은 얼마?!!
# 최대로 할인을 받기 위해서는 큰 금액을 큰 할인율의 쿠폰으로 사는 것

shop_prices = [30000, 2000, 1500000]  # 가격
user_coupons = [20, 40]  # 쿠폰


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)  # prices를 내림차순으로 정렬 -> 큰 값을 큰 할인율로 받아야 비교적 저렴하게 구입할 수 있으므로
    coupons.sort(reverse=True) # coupons를 내림차순으로 정렬

    price_index = 0
    coupon_index = 0
    max_discounted = 0

    # prices와 coupons를 같은 자리 인덱스끼리 연산해 주기 위해 while문 실행
    # for문은 두개의 배열의 수가 다를 수 있기 때문에 while문이 더 적합
    while price_index < len(prices) and coupon_index < len(coupons):  # price_index와 coupon_index가 각각의 길이보다 작을 경우까지만 반복
        max_discounted += prices[price_index] * (100 - coupons[coupon_index]) / 100  # price와 할인율을 각각 곱해줌
        price_index += 1
        coupon_index += 1

    # 남은 price는 따로 더해줌 (copon은 할인율이기때문에 copon만 남아도 저장할 필요없음)
    while price_index < len(prices):
        max_discounted += prices[price_index]
        price_index += 1

    return int(max_discounted)


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.
