import pickle
from constants import DEFAULT_DATA
import os

"""Сохранение данных в базу данных pickle"""
if os.path.exists('points.pkl') and os.path.getsize('points.pkl') > 0:
    try:
        with open('points.pkl', 'rb') as fp:
            DATA = pickle.load(fp)

    except FileNotFoundError:
        DATA = DEFAULT_DATA

else:
    DATA = DEFAULT_DATA

