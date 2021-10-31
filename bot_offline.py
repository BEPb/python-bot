# python3
# bot for offline game on hrome

import numpy as np
import cv2   # работа с изображениями
from mss.windows import MSS as msss  # модуль обработки скрина без сохранения на диск
import mss.tools
import os  # для работы с командной строкой (определение экрана)
import time  # работа со временем
import pyautogui as pg
import logging  # модуль логирования
import subprocess  # Запуск приложений windows
import keyboard  # работа с нажатиями клавиш


def screen_resolution():  # функция определения разрешения экрана
    global screen_width_x, screen_height_y  # определяем глобальные переменные
    cmd = 'wmic path Win32_VideoController get CurrentHorizontalResolution,CurrentVerticalResolution'  # вызываем
    # командную строку и через нее определяем разрешение экрана
    size_tuple = tuple(map(int, os.popen(cmd).read().split()[-2::]))  # считываем данные из командной строки
    screen_width_x = size_tuple[0]  # сохраняем значения расширения экрана по оси х
    screen_height_y = size_tuple[1]  # сохраняем значения расширения экрана по оси у
    logging.info('%s screen width', screen_width_x)  # запись в лог файл ширины экрана
    logging.info('%s screen height', screen_height_y)  # запись в лог файл высоты экрана
    return screen_width_x, screen_height_y  # возвращение глобальных переменных


def startlnk():  # функция запуска приложения
    subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe')  # запуск приложения
    time.sleep(1)  # время ожидания запуска
    time.sleep(1)  # время ожидания
    keyboard.send("Ctrl + Shift + T")  # открывает последнюю страницу
    keyboard.send("windows+up")  # разворачивает приложение на все окно
    time.sleep(1)  # время ожидания
    keyboard.send("Ctrl + Shift + R")  # обновляем страницу
    time.sleep(1)  # время ожидания
    keyboard.send("space")  # начинаем игру нажимая пробел


def ss(template):  # функция определения координат изображения
    global zero, screen_width_x, screen_height_y, buttonx, buttony  # определяем глобальные переменные
    try:
        buttonx, buttony = pg.locateCenterOnScreen(template, region=(0, 0, screen_width_x, screen_height_y),
                                                   confidence=0.7)  # опеределяем координаты нашего дракона
        # pg.moveTo(buttonx, buttony)  # перемещается к искомомму изображению
        # pg.doubleClick(buttonx, buttony)  # дважды нажимает на искомое изображение
        time.sleep(1)  # ждем 1 сек.
        return buttonx, buttony   # возвращаем переменные
    except TypeError:  # в том случае если изображение не найдено
        return zero  # возвращаем ноль

 
def process_image(original_image):
    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)
    return processed_image


def main():
    sct = msss()  # модуль обработки скрина без сохранения на диск
    last_time = time.time()  # определяем текущее время
    space_time = time.time()  # определяем время нажатия пробела

    while(True):
        img = sct.grab(monitor)  # модуль обработки скрина без сохранения на диск
        # Save to the picture file
        # output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)  # определяем формат изображения
        # mss.tools.to_png(img.rgb, img.size, output=output)  # сохраняем изображение
        # print(output)  # название файла
        # print('loop took {} seconds'.format(time.time() - last_time))  # отображаем время между анализом изображения
        # last_time = time.time()
        img = np.array(img)  # преобразуем изображение в табличные данные
        processed_image = process_image(img)  # запускаем функцию
        mean = np.mean(processed_image)  # переменная которая определяет смену изображения в указанной зоне
        # print('mean = ', mean)
        delta_time = time.time() - space_time  # разница по времени между нажатиями кнопки пробел

        if not mean == float(0):  # если картинка в указанное области менялась, то..
            pg.press('space')  # нажатие на пробел
            space_time = time.time()  # определяем время нажатия пробела

        if delta_time > 15:  # если долго (более 15 секунд) не нажимают на пробел значит игра закончена
            pg.press('space')  # для запуска новой игры нажимаем пробел
            space_time = time.time()  # определяем время нажатия пробела
            delta_time = (time.time() - last_time)/60  # длительность игры в минутах
            logging.info('%s game time', delta_time)  # запись в лог файл ширины экрана

        if cv2.waitKey(25) & 0xFF == ord('q'):  # ожидает 25 милисекунд, при нажатии на клавишу 'q'
            print("Ты сказал стоп слово), извращения заканчиваем....")
            cv2.destroyAllWindows()
            break  # выход из цикла

# variables (переменные)
screen_width_x = 0  # ширина экрана, координата х - максимальная
screen_height_y = 0  # высота экрана, координата у - максимальная
zero = 0  # пустая переменная
buttonx = 100  # координаты объекта по оси х
buttony = 100  # координаты объекта по оси у


# описываем параметры логирования
logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Start game and logged in')
# примеры логирования с разными уровнями важности
# logging.info('This is an info message')
# logging.debug('This is a debug message')
# logging.warning('This will get logged to a file')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


# исполняемый код
startlnk()  # запуск приложения хром
screen_resolution()  # определяем разрешение экрана
active_dir = 'media/' + str(screen_width_x) + 'x' + str(screen_height_y) + '/'  # активная папка для соответствующего
# разрешения
print(screen_width_x, screen_height_y)
ss(active_dir + "dragon.png")  # определение координат дракона на экране
print(buttonx, buttony)
x1 = int(buttonx + (screen_width_x * (150/1920)))
y1 = int(buttony - (screen_height_y * (15/1920)))
x2 = int(screen_width_x * (30/1920))
y2 = int(screen_height_y * (30/1920))
monitor = {'top': y1, 'left': x1, 'width': x2, 'height': y2}  # расчет зоны реакции


if __name__ == "__main__":
    main()