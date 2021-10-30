# python3
# bot for offline game on hrome

import numpy as np
import cv2
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
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, screen_width_x, screen_height_y), confidence=0.7)
        # pg.moveTo(buttonx, buttony)
        # pg.doubleClick(buttonx, buttony)
        time.sleep(1)
        return buttonx, buttony
    except TypeError:
        return zero

 
def process_image(original_image):
    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)
    return processed_image


def main():
    sct = mss()
    last_time = time.time()

    while(True):
        img = sct.grab(mon)
        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        img = np.array(img)
        processed_image = process_image(img)
        mean = np.mean(processed_image)
        print('mean = ', mean)
 
        if not mean == float(0):
            pg.press('space')
 
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

# variables (переменные)
screen_width_x = 0  # ширина экрана, координата х - максимальная
screen_height_y = 0  # высота экрана, координата у - максимальная
zero = 0
buttonx = 0  # координаты объекта по оси х
buttony = 0  # координаты объекта по оси у


# описываем параметры логирования
logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Start game and logged in')
# примеры логирования с разными уровнями важности
# logging.info('This is an info message')
# logging.debug('This is a debug message')
# logging.warning('This will get logged to a file')
# logging.error('This is an error message')
# logging.critical('This is a critical message')



def startlnk():  # функция запуска приложения
    subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe')  # запуск приложения
    time.sleep(1)  # время ожидания запуска
    time.sleep(1)  # время ожидания
    keyboard.send("Ctrl + Shift + T")  # открывает последнюю страницу
    keyboard.send("windows+up")  # разворачивает приложение на все окно
    # keyboard.send("Ctrl + Shift + R")  # обновляем страницу
    time.sleep(1)  # время ожидания



# исполняемый код

startlnk()  # запуск приложения хром
screen_resolution()  # определяем разрешение экрана
active_dir = 'media/' + str(screen_width_x) + 'x' + str(screen_height_y) + '/'  # активная папка для соответствующего
# разрешения
print(screen_width_x, screen_height_y)
ss(active_dir + "dragon.png")  # определение координат дракона на экране
print(buttonx, buttony)
mon = {'top': buttonx + 10, 'left': (buttony - 15), 'width': 85, 'height': 30}  # расчет зоны реакции
# для прыжка


if __name__ == "__main__":
    main()