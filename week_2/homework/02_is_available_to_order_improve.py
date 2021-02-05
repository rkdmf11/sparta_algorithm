shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

"""
이 문제는 단순히 특정한 문자열이 배열에 존재하는지만 확인하면 됨
정렬을 할 필요없이, **집합 자료형**을 사용하면 쉽게 해결 가능
"""

def is_available_to_order(menus, orders):
    menus_set = set(menus)  # set은 집합을 의미하며, 중복을 허용하지 않는 자료형

    for order in orders:
        if order not in menus_set:
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)
