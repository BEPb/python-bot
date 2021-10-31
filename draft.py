# python3
# bot for offline game on hrome (определение зоны анализа)

import cv2  # работа с изображениями
from mss.windows import MSS as mss
import os  # для работы с командной строкой (определение экрана)
import time  # работа со временем
import pyautogui as pg
import logging  # модуль логирования
import subprocess  # Запуск приложений windows
import keyboard  # работа с нажатиями клавиш

def screen_resolution():  # функция определения разрешения экрана
    global screen_width_x, screen_height_y
    cmd = 'wmic path Win32_VideoController get CurrentHorizontalResolution,CurrentVerticalResolution'
    size_tuple = tuple(map(int, os.popen(cmd).read().split()[-2::]))
    screen_width_x = size_tuple[0]
    screen_height_y = size_tuple[1]
    logging.info('%s screen width', screen_width_x)  # запись в лог файл ширины экрана
    logging.info('%s screen height', screen_height_y)  # запись в лог файл высоты экрана
    return screen_width_x, screen_height_y  # возвращение глобальных переменных

def ss(template):  # функция определения координат изображения
    global zero, screen_width_x, screen_height_y, buttonx, buttony
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, screen_width_x, screen_height_y),
                                                   confidence=0.7)
        time.sleep(1)
        return buttonx, buttony
    except TypeError:
        return zero


# variables (переменные)
screen_width_x = 0  # ширина экрана, координата х - максимальная
screen_height_y = 0  # высота экрана, координата у - максимальная
zero = 0
buttonx = 100  # координаты объекта по оси х по умолчанию
buttony = 100  # координаты объекта по оси у по умолчанию


def startlnk():  # функция запуска приложения
    subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe')  # запуск приложения
    time.sleep(1)  # время ожидания запуска
    time.sleep(1)  # время ожидания
    keyboard.send("Ctrl + Shift + T")  # открывает последнюю страницу
    keyboard.send("windows+up")  # разворачивает приложение на все окно
    # keyboard.send("Ctrl + Shift + R")  # обновляем страницу
    time.sleep(1)  # время ожидания


# исполняемый код
screen_resolution()
startlnk()  # запуск приложения хром
active_dir = 'media/' + str(screen_width_x) + 'x' + str(screen_height_y) + '/'  # активная папка для соответствующего
# разрешения
print(screen_width_x, screen_height_y)
ss(active_dir + "dragon.png")  # определение координат дракона на экране
print(buttonx, buttony)
mon = {'top': (buttonx + 10), 'left': (buttony - 15), 'width': 85, 'height': 30}  # расчет зоны реакции

screen = pg.screenshot('screenshot.png')  # скрин всего экрана
# pyautogui.screenshot('screenshot.png',region=(0,0, 300, 400)) # скрин области экрана



path = r'C:\pyProject\python-bot\screenshot.png'  # считываем изображение
image = cv2.imread(path, 0)  # считываем изображение в черно-белом с оттенками серого режиме
window_name = 'Image'  # Задаем имя окна, где будет отображаться изображение
start_point = (buttonx + 25, buttony - 20)  # Верхний левый угол прямоугольника
end_point = (buttonx + 85, buttony + 20)  # Нижний правый угол прямоугольника
color = (0, 0, 0)  # Черный цвет BGR
thickness = 1  # Толщина линии 1 пиксель (-1 заполнит всю форму)
image = cv2.rectangle(image, start_point, end_point, color, thickness)  # рисуем прямоугольник
cv2.imshow(window_name, image)  # Отображение результата в отдельном окне
cv2.waitKey(0)
cv2.destroyAllWindows()


# # Создать черную рамку, uint8 - тип линии, 8 подключено
# img=np.zeros((512,512,3),np.uint8)
# img=cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
#  # Отображение графики в окне
# cv2.imshow("image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
