shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "새우만두"]


def is_available_to_order(menus, orders):
    menus.sort()
    print(menus, orders)

    for order in orders:
        if not available_order(order, menus):  # 해당함수가 True가 아니면 실행
            return False
    return True


def available_order(target, array):
    count_min = 0
    count_max = len(array) - 1
    count_guess = (count_min + count_max) // 2

    while count_min <= count_max:
        print('메뉴 = ', array, target)
        if array[count_guess] == target:
            print('참 = ', array[count_guess], target)
            return True
        elif array[count_guess] < target:
            print('타겟이 큼 = ', array[count_guess], target)
            count_min = count_guess + 1
        else:
            count_max = count_guess - 1
            print('타겟이 작음 = ', array[count_guess], target)
        count_guess = (count_min + count_max) // 2


result = is_available_to_order(shop_menus, shop_orders)
print(result)
