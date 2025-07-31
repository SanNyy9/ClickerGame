from data_saving import DATA
from windows import main_window
from classes import RepeatTimer
import pygame
"""Функция увеличивает скорость добавления поинтов в секунду и сохраняет в базу данных"""
def increase_tank():
    DATA['general_tank'] += DATA['efficiency']

if __name__ == "__main__":
    pygame.init()
    timer = RepeatTimer(1, increase_tank)
    timer.start()
    main_window()