from classes import WindowForButtons, ImageButton, Button
from constants import with_symbols, SUITABLE_BG, DICT_FOR_UPGRDS_Y
from data_saving import DATA
import pygame

"""Функция открытия главного экрана с расположением всех кнопок"""
def main_window():
    button_list = []
    main_window = main_window_instance
    map_upg_str_set_tap_list = []

    BUTTON_SIZE = (67, 67)
    TAP_BUTTON_SIZE = (350, 438)
    UNCKICKABBLE_SIZE = (50, 50)

    map_button = ImageButton(x=18, y=857, image_path='pics/map.png', size=BUTTON_SIZE)
    upgrades_button = ImageButton(x=131, y=857, image_path='pics/upgrade.png', size=BUTTON_SIZE)
    store_button = ImageButton(x=244, y=857, image_path='pics/store.png', size=BUTTON_SIZE)
    settings_button = ImageButton(x=347, y=857, image_path='pics/settings.png', size=BUTTON_SIZE)
    tap_button = ImageButton(x=45, y=250, image_path='pics/blueball.png', size=TAP_BUTTON_SIZE)

    map_upg_str_set_tap_list.extend([map_button, upgrades_button, store_button, settings_button, tap_button])

    points_amount = Button(size=UNCKICKABBLE_SIZE, location=(180, 687), text=f'{with_symbols(DATA, 'general_tank')}', color=SUITABLE_BG)
    efficiency_amount = Button(size=UNCKICKABBLE_SIZE, location=(180, 72), text=f'{with_symbols(DATA, 'efficiency')}', color=SUITABLE_BG)
    gems_amount = Button(size=UNCKICKABBLE_SIZE, location=(330, 72), text=f'{with_symbols(DATA, 'gems')}', color=SUITABLE_BG)
    total_click = Button(size=UNCKICKABBLE_SIZE, location=(28, 72), text=f'{with_symbols(DATA, 'summ_koff')}', color=SUITABLE_BG)

    button_list.extend([points_amount, efficiency_amount, gems_amount, total_click])

    main_window.create_window(bg='pics/main_window.png', button_list=button_list, map_upg_str_set_tap_list=map_upg_str_set_tap_list)

    pygame.display.flip()

"""Функция открытия окна с картой"""
def window_for_map_button():
    map_buttons = []
    back_button_list = []
    map_window = main_window_instance

    HOODS_CORD_DICT = {
        'centre': (185, 565),
        'suburb': (218, 38),
        'corner': (328, 375),
        'seafront': (55, 385),
        'left': (50, 800),
        'right': (240, 800)

    }
    centre_button = ImageButton.hood_buttons(x=HOODS_CORD_DICT['centre'][0], y=HOODS_CORD_DICT['centre'][1])
    suburb_button = ImageButton.hood_buttons(x=HOODS_CORD_DICT['suburb'][0], y=HOODS_CORD_DICT['suburb'][1])
    corner_button = ImageButton.hood_buttons(x=HOODS_CORD_DICT['corner'][0], y=HOODS_CORD_DICT['corner'][1])
    seafront_button = ImageButton.hood_buttons(x=HOODS_CORD_DICT['seafront'][0], y=HOODS_CORD_DICT['seafront'][1])
    left_button = ImageButton.hood_buttons(x=HOODS_CORD_DICT['left'][0], y=HOODS_CORD_DICT['left'][1])
    right_button = ImageButton.hood_buttons(x=HOODS_CORD_DICT['right'][0], y=HOODS_CORD_DICT['right'][1])

    map_buttons.extend([centre_button, suburb_button, corner_button, seafront_button, left_button, right_button])

    back_button = ImageButton.method_for_back_button()
    back_button_list.append(back_button)

    map_window.create_window(bg='pics/map_window.png', back_button=back_button_list, map_buttons=map_buttons)

"""Функция открытия окна с улучшениями"""
def window_for_upgrades_button():
    upgrades_window_per_click = main_window_instance
    strings_list = []
    upgrades_list = []
    back_button_list = []
    DICT_FOR_LINES = {
        1: (190, 200),
        2: (190, 292),
        3: (190, 384),
        4: (190, 478),
        5: (190, 570),
        6: (190, 664),
        7: (190, 757),
        8: (190, 852)
    }
    X_FOR_UPGRDS = 347

    """Два цикла, которые создают полосы, не повторяя код"""
    for number in range(1, len(DICT_FOR_LINES)+1):
        line = Button.method_for_main_strings(location=(DICT_FOR_LINES[number]), text=f'{with_symbols(DATA, f'cost_{number}_per_click')}')
        strings_list.extend([line])

    for number in range(1, len(DICT_FOR_UPGRDS_Y)+1):
        button_buy_upgrade = ImageButton.upgrades_button_method(x=X_FOR_UPGRDS, y=DICT_FOR_UPGRDS_Y[number])
        upgrades_list.extend([button_buy_upgrade])

    back_button = ImageButton.method_for_back_button()
    back_button_list.append(back_button)

    button_per_second = ImageButton(x=280, y=90, image_path='pics/per sec.png', size=(150, 60))
    upgrades_list.append(button_per_second)

    upgrades_window_per_click.create_window(upgrades_list=upgrades_list, strings_list=strings_list,
                                            back_button=back_button_list, bg='pics/boost_per_click_window.png')

"""Функция открытия окна с магазином (пока ничего не сделал)"""
def window_for_store_button():
    back_button_list = []
    back_button = ImageButton.method_for_back_button()
    back_button_list.append(back_button)

    store_window = main_window_instance
    store_window.create_window(back_button=back_button_list, bg='pics/store_window.png')

"""Функция открытия окна с настройками (пока ничего не сделал)"""
def window_for_settings_button():
    back_button_list = []
    back_button = ImageButton.method_for_back_button()
    back_button_list.append(back_button)

    settings_window = main_window_instance
    settings_window.create_window(back_button=back_button_list, bg='pics/settings_window.png')

"""Функция, похожая на window_for_upgrades_button (может можно их объеденить), для открытия раздела улучшения в секунду в окне улучшений"""
def window_per_second():
    upgrades_window_per_second = main_window_instance
    strings_list = []
    upgrades_list_per_second = []
    back_button_list = []

    back_button = ImageButton.method_for_back_button()
    back_button_list.append(back_button)

    DICT_FOR_LINES = {
        1: (230, 200),
        2: (230, 292),
        3: (230, 384),
        4: (230, 478),
        5: (230, 570),
        6: (230, 664),
        7: (230, 757),
        8: (230, 852)
    }
    X_FOR_UPGRDS = 347

    """Два цикла, которые создают полосы, не повторяя код"""
    for number in range(1, len(DICT_FOR_LINES) + 1):
        line = Button.method_for_main_strings(location=(DICT_FOR_LINES[number]),
                                              text=f'{with_symbols(DATA, f'cost_{number}_per_second')}')
        strings_list.extend([line])

    for number in range(1, len(DICT_FOR_UPGRDS_Y) + 1):
        button_buy_upgrade = ImageButton.upgrades_button_method(x=X_FOR_UPGRDS, y=DICT_FOR_UPGRDS_Y[number])
        upgrades_list_per_second.extend([button_buy_upgrade])

    button_per_second = ImageButton(x=110, y=90, image_path='pics/per click.png', size=(150, 60))
    upgrades_list_per_second.append(button_per_second)

    upgrades_window_per_second.create_window(strings_list=strings_list, upgrades_list_per_second=upgrades_list_per_second,
                                             back_button=back_button_list, bg='pics/boost_per_second_window.png')

"""Функция открытия окна с районами на карте"""
def window_for_map_hoods(hood_name, cost):
    hood_window = main_window_instance
    hood_info_window = []
    back_button_list=[]

    name_button = Button(size=(150, 50), location=(150, 250), color=(255, 255, 255, 0), text=hood_name)
    cost_button = Button(size=(50, 50), location=(200, 510), color=SUITABLE_BG, text=cost)

    hood_info_window.extend([name_button, cost_button])
    back_button = ImageButton.method_for_back_button()
    back_button_list.append(back_button)

    back_button = Button(size=(70, 70), location=(30, 30), color=(255, 255, 255, 0))
    hood_info_window.append(back_button)

    hood_window.create_window(back_button_for_map=back_button_list, bg='pics/hoods_window.png', hood_info_window=hood_info_window)

"""Это функция решает баги"""
def setup_window_functions(window_instance):
    window_instance.register_window_functions(
        main_window=main_window,
        map_window=window_for_map_button,
        upgrades_window=window_for_upgrades_button,
        store_window=window_for_store_button,
        settings_window=window_for_settings_button,
        per_second_window=window_per_second,
        map_hoods_window=window_for_map_hoods
    )

main_window_instance = WindowForButtons()
setup_window_functions(main_window_instance)