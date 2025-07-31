import pygame
import math

pygame.init()

# Константы игры
POINTS_PER_CLICK = {
    "button_buy_upgrade1": 1,
    'button_buy_upgrade2': 3,
    'button_buy_upgrade3': 5,
    'button_buy_upgrade4': 10,
    'button_buy_upgrade5': 25,
    'button_buy_upgrade6': 50,
    'button_buy_upgrade7': 100,
    'button_buy_upgrade8': 500
}

POINTS_PER_SECOND = {
    'per_second1': 0.1,
    'per_second2': 0.3,
    'per_second3': 1,
    'per_second4': 3,
    'per_second5': 5,
    'per_second6': 7,
    'per_second7': 10,
    'per_second8': 15,
}

MULTIPLY_COEFF = 1.1
SUITABLE_BG = (178, 219, 243)

DEFAULT_DATA = {
    'general_tank': 1000000,
    'efficiency': 1,
    'gems': 0,
    'summ_koff': 1,
    'cost_1_per_click': 100,
    'cost_2_per_click': 1000,
    'cost_3_per_click': 5000,
    'cost_4_per_click': 50000,
    'cost_5_per_click': 200000,
    'cost_6_per_click': 5000000,
    'cost_7_per_click': 10000000,
    'cost_8_per_click': 100000000,
    'cost_1_per_second': 500,
    'cost_2_per_second': 2000,
    'cost_3_per_second': 10000,
    'cost_4_per_second': 100000,
    'cost_5_per_second': 400000,
    'cost_6_per_second': 1000000,
    'cost_7_per_second': 2000000,
    'cost_8_per_second': 20000000,
}

DICT_FOR_UPGRDS_Y = {
        1: 194,
        2: 284,
        3: 378,
        4: 470,
        5: 565,
        6: 660,
        7: 752,
        8: 845
    }

def with_symbols(needed_list: list, const: str):
    """Форматирует число в сокращенный вид"""

    amount = int(math.floor(needed_list[const]))

    if 1000 <= amount <= 999999:
        cost = f'{amount // 1000}K'

    elif (10 ** 6) <= amount < (10 ** 9):
        cost = f'{amount // (10 ** 6)}M'

    elif amount > (10 ** 9):
        cost = f'{amount // (10 ** 9)}B'

    else:
        cost = amount

    return cost