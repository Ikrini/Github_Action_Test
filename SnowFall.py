#snowfall

import pygame
import random                      #random library
import sys
import time

#обозначаем глобальные переменные
MAX_X = 1920
MAX_Y = 1080
MAX_SNOW = 100             #snowflakes count
SNOW_SIZE = 64

class Snow():
    def __init__(self, x, y):
        self.x = x                #внутренний x = внешнему x
        self.y = y
        self.speed = random.randint(1, 3)            #скорость падения снижинки = рандомнову числу от 1вкл. до 3вкл.
        self.img_num = random.randint(1, 4)          #переменную приравняли к рандомному числу от 1вкл до 4 вкл
        self.image_filename = "snow-" + str(self.img_num) + ".png"    ##берём рандомную фотку от 1 до 4 (так как в названиях фоток отличаются только номера от 1 до 4)
        self.image = pygame.image.load(self.image_filename).convert_alpha()                #загрузили фотку
        self.image = pygame.transform.scale(self.image, (SNOW_SIZE, SNOW_SIZE))      #картинка = уменьшить картинку(переменная картинки, (размер, размер))

    def move_snow(self):                     #метод для движения снежинки
        self.y = self.y + self.speed         #снежинка по y (вниз) = снежинка вниз + скорость падения (указана выше от 1 до 3)
        if self.y > MAX_Y:                  #если снежинка по y ушла вниз полностью
            self.y = (0 - SNOW_SIZE)         #тогда рисуем её сверху плавное появление

        i = random.randint(1, 3)           #типа флаг для x
        if i == 1:         #move right
            self.x += 1
            if self. x > MAX_X:                   #если вышел за рамки экарана вправо
                self.x = (0 - SNOW_SIZE)           #тогда плавно появится слева
        elif i == 2:                         #move left
            self.x -= 1
            if self.x < (0 - SNOW_SIZE):     #если картинка снежинки ушла левее нуля
                self.x = MAX_X               #тогда она вырисовывается спарва (1920)

    def draw_snow(self):
        screen.blit(self.image, (self.x, self.y))              #выбрасываем на экран картинку (и где выкинуть - размер изображения)

def initialize_snow(max_snow, snowfall):                        #функция будет создавать наши снежинки и давать им рандомные положения на экране (случ полж x и y)
    for i in range(0, max_snow):                      #сколько снежинок хотим (от нуля до 100 (MAX_SNOW = 100)
        xx = random.randint(0, MAX_X)                 #xx = рандомное положение (от 0 до 1920) будет появляться снежинка по x
        yy = random.randint(0, MAX_Y)
        snowfall.append(Snow(xx, yy))              #добавляем в массив объекты

def check_for_exit():                              #метод для выхода из функции
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:           #реагируем на случай нажатия любой клавиши
            sys.exit()

#-----------------------MAIN----------------------

pygame.init()

screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)       #выводим  на полный экран

bg_color = (0, 0, 0)                                                      #делайм фон чёрным
snowfall = []                    #создаём пустой массив для наших снежинок


#initialize_pygame(MAX_X, MAX_Y)                     #перекинули в функцию расширение нашего экрана. Функция берёт размер (заданный)

initialize_snow(MAX_SNOW, snowfall)                                 #функция берёт количество снежинок и куда их отправить

while True:
    screen.fill(bg_color)            #заполнить скрин назначенным цветом (0, 0, 0)
    check_for_exit()                 #есть ли нажатие клавиши (для выхода) ?
    for i in snowfall:               #проходим по массиву где лежат снежинки
        i.move_snow()                #двигаем снежинки
        i.draw_snow()                #рисуем снежинки
    pygame.display.flip()

