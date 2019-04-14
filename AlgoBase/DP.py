from typing import Dict, List


def packet(goods: List[dict], packet_weight):

    arr = [[0] * (packet_weight+1) for i in range(len(goods))]

    for i in range(len(goods)):
        print(goods[i])
        for j in range(1, packet_weight+1):
            if j < goods[i]['weight']:
                if i <= 0:
                    pass
                else:
                    arr[i][j] = arr[i-1][j]
            else:
                if i <= 0:
                    arr[i][j] = goods[i]['value']
                else:
                    new_value = goods[i]['value'] + arr[i-1][j-goods[i]['weight']]
                    arr[i][j] = new_value if new_value > arr[i-1][j] else arr[i-1][j]

    return arr

if __name__ == '__main__':
    packet_weight = 4
    goods = []
    # goods.append({'weight': 1, 'value': 6})
    # goods.append({'weight': 2, 'value': 5})
    # goods.append({'weight': 2, 'value': 9})
    # goods.append({'weight': 1, 'value': 3})
    # goods.append({'weight': 3, 'value': 10})

    goods.append({'weight': 1, 'value': 7})
    goods.append({'weight': 1, 'value': 6})
    goods.append({'weight': 2, 'value': 9})
    goods.append({'weight': 4, 'value': 9})
    goods.append({'weight': 1, 'value': 8})

    maxinumvalue = packet(goods, packet_weight)
    print(maxinumvalue)

