import pygame
import threading
from constants import SUITABLE_BG, POINTS_PER_CLICK, MULTIPLY_COEFF, POINTS_PER_SECOND, with_symbols
from data_saving import DATA
import pickle

class RepeatTimer(threading.Timer):
    """Класс для постоянного добавления поинтов"""

    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


class Button:
    """Класс для создания некликабельных кнопок на экране"""
    def __init__(self, size: tuple, location: tuple, text_color: tuple = (0, 0, 0), text: str = '',
                 color: tuple = (255, 255, 255), font: str = None):
        self.size = size
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(font, 24) if font else pygame.font.SysFont(None, 24)
        self.location = location
        self.button_surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self.button_rect = pygame.Rect(self.location, self.size)
        self.button_surf = self.font.render(self.text, True, self.text_color)

    def create_button(self):
        self.button_surface.fill(self.color)
        self.button_surface.blit(self.button_surf,
                               [
                                   self.button_rect.width / 2 - self.button_surf.get_rect().width / 2,
                                   self.button_rect.height / 2 - self.button_surf.get_rect().height / 2
                               ])
        pygame.display.get_surface().blit(self.button_surface, self.button_rect)

    @classmethod
    def method_for_main_strings(cls, location: tuple, text: str):
        return cls(size=(70, 50), location=location, text=text, color=SUITABLE_BG)


class ImageButton:
    """Класс для создания кликабельных кнопок на экране (можно сделать наследование с классом Button"""

    def __init__(self, x: int, y: int, image_path: str, size: tuple = (69, 69)):
        try:
            self.image = pygame.image.load(image_path)
            self.size = size
            self.image = pygame.transform.scale(self.image, size)
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.is_pressed = False
            self.pressed_size = (self.size[0] - 10, self.size[1] - 10)
        except pygame.error as e:
            print(f"Error loading image: {e}")
            self.image = pygame.Surface(size)
            self.image.fill((255, 0, 255))
            self.rect = self.image.get_rect(topleft=(x, y))
            self.is_pressed = False
            self.pressed_size = size

    def draw(self, surface):
        if self.is_pressed:
            current_image = pygame.transform.scale(self.image, self.pressed_size)
            pos = (self.rect.x + (self.size[0] - self.pressed_size[0]) // 2,
                   self.rect.y + (self.size[1] - self.pressed_size[1]) // 2)
        else:
            current_image = self.image
            pos = self.rect.topleft
        surface.blit(current_image, pos)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    @staticmethod
    def method_for_back_button():
        return ImageButton(x=30, y=30, image_path='pics/back_button.png', size=(70, 70))

    @classmethod
    def hood_buttons(cls, x: int, y: int):
        return cls(x, y, image_path='pics/spot.png', size=(60, 60))

    @classmethod
    def upgrades_button_method(cls, x: int, y: int):
        return cls(x, y, image_path='pics/per click4.png', size=(60, 60))


class WindowForButtons:
    """Класс главного экрана на котором вся логика окон и кнопок"""
    def __init__(self, size=(440, 956), window_name='', background_color=(255, 255, 255)):
        self.size = size
        self.screen = pygame.display.set_mode(self.size)
        self.window_name = window_name
        self.background_color = background_color
        self.pressed_buttons = {}
        self.main_window_func = None
        self.map_window_func = None
        self.upgrades_window_func = None
        self.store_window_func = None
        self.settings_window_func = None
        self.per_second_window_func = None
        self.map_hoods_window_func = None

    """Метод, помогающий избежать багов"""
    def register_window_functions(self, main_window, map_window, upgrades_window, store_window, settings_window,
                                  per_second_window, map_hoods_window):
        self.main_window_func = main_window
        self.map_window_func = map_window
        self.upgrades_window_func = upgrades_window
        self.store_window_func = store_window
        self.settings_window_func = settings_window
        self.per_second_window_func = per_second_window
        self.map_hoods_window_func = map_hoods_window

    """Метод в котором происходит открытие всех окон"""
    def create_window(self, bg=None, button_list:list=[], strings_list:list=[], upgrades_list_per_second:list=[], upgrades_list:list=[],
                      back_button:list=[], map_buttons:list=[], map_upg_str_set_tap_list:list=[], back_button_for_map:list=[], hood_info_window:list=[]):

        pygame.display.set_caption(self.window_name)
        self.screen.fill(self.background_color)

        clickable_buttons = []
        not_clickable_buttons = []

        clickable_buttons.extend([upgrades_list_per_second, upgrades_list, map_buttons,
                            map_upg_str_set_tap_list, back_button, back_button_for_map])

        not_clickable_buttons.extend([strings_list, button_list, hood_info_window])

        if bg is not None:
            bg = pygame.image.load(bg)
            bg = pygame.transform.scale(bg, (440, 956))
            self.screen.blit(bg, (0, 0))

        for button_group in not_clickable_buttons:
            if button_group:
                for buttons in button_group:
                    buttons.create_button()

        while True:
            if button_list:
                self.update_data(button_list, 0, 'general_tank')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                    if back_button:
                        if back_button[0].is_clicked(event.pos):
                            self.main_window_func()

                    if map_upg_str_set_tap_list:

                        if map_upg_str_set_tap_list[0].is_clicked(event.pos):
                            self.map_window_func()

                        if map_upg_str_set_tap_list[1].is_clicked(event.pos):
                            self.upgrades_window_func()

                        if map_upg_str_set_tap_list[2].is_clicked(event.pos):
                            self.store_window_func()

                        if map_upg_str_set_tap_list[3].is_clicked(event.pos):
                            self.settings_window_func()

                        if map_upg_str_set_tap_list[4].is_clicked(event.pos):
                            DATA['general_tank'] += DATA['summ_koff']
                            self.update_data(button_list, 0, 'general_tank')
                            map_upg_str_set_tap_list[4].is_pressed = True

                    if upgrades_list:
                        for indx in range(len(upgrades_list) - 1):

                            per_click = f'cost_{indx + 1}_per_click'
                            buy_upgrade = f'button_buy_upgrade{indx + 1}'

                            if DATA['general_tank'] >= DATA[per_click]:
                                if upgrades_list[indx].is_clicked(event.pos):
                                    DATA['summ_koff'] += POINTS_PER_CLICK[buy_upgrade]
                                    DATA['general_tank'] -= DATA[per_click]
                                    DATA[per_click] = int(round(DATA[per_click] * MULTIPLY_COEFF))
                                    self.update_data(strings_list, indx, per_click)

                        if upgrades_list[8].is_clicked(event.pos):
                            self.per_second_window_func()

                    if upgrades_list_per_second:
                        for indx in range(len(upgrades_list_per_second) - 1):

                            per_sec = f'per_second{indx + 1}'
                            cost_per_sec = f'cost_{indx + 1}_per_second'

                            if DATA['general_tank'] >= DATA[cost_per_sec]:
                                if upgrades_list_per_second[indx].is_clicked(event.pos):
                                    DATA['efficiency'] += POINTS_PER_SECOND[per_sec]
                                    DATA['general_tank'] -= DATA[cost_per_sec]
                                    DATA[cost_per_sec] = int(round(DATA[cost_per_sec] * MULTIPLY_COEFF))
                                    self.update_data(strings_list, indx, cost_per_sec)

                        if upgrades_list_per_second[8].is_clicked(event.pos):
                            self.upgrades_window_func()

                    if map_buttons:
                        DICT_FOR_HOODS = {
                            0: ['Centre', '16M'],
                            1: ['Suburban', '16M'],
                            2: ['Hood', '16M'],
                            3: ['Seafront', '16M'],
                            4: ['Seafront', '16M'],
                            5: ['Living', '16M'],
                            6: ['Mall', '16M']
                        }
                        for index in range(len(DICT_FOR_HOODS)):
                            if map_buttons[index].is_clicked(event.pos):
                                self.map_hoods_window_func(hood_name=DICT_FOR_HOODS[index][0], cost=DICT_FOR_HOODS[index][1])

                    if back_button_for_map:
                        if back_button_for_map[0].is_clicked(event.pos):
                            self.map_window_func()

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    for button_group in clickable_buttons:
                        if button_group:
                            for buttons in button_group:
                                buttons.is_pressed = False

            for button_group in clickable_buttons:
                if button_group:
                    for buttons in button_group:
                        buttons.draw(self.screen)

            pygame.display.flip()

    """Функция, которая обновляет значение некликабельный кнопок"""
    def update_data(self, needed_list:list, num: int, const: str):
        try:
            with open('points.pkl', 'wb') as fp:
                pickle.dump(DATA, fp)
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")

        cost = with_symbols(DATA, const)
        needed_list[num].button_surf = needed_list[num].font.render(f'{cost}', True, needed_list[num].text_color)
        needed_list[num].button_surface.fill(needed_list[num].color)
        needed_list[num].button_surface.blit(needed_list[num].button_surf,
                                             [
                                                 needed_list[num].button_rect.width / 2 - needed_list[
                                                     num].button_surf.get_rect().width / 2,
                                                 needed_list[num].button_rect.height / 2 - needed_list[
                                                     num].button_surf.get_rect().height / 2
                                             ])
        self.screen.blit(needed_list[num].button_surface, needed_list[num].button_rect)