import pygame
import sys
import copy
import random

pygame.init()
screen = pygame.display.set_mode((1000, 500))
FPS = 30
fpsClock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)


# ____________________________________________________________________func_start
# ________________________________________________________________

def run():
    # задание параметров базового экрана
    global screen
    screen.fill((192, 220, 192))
    pygame.display.flip()

    pygame.display.set_caption('Bulls & Cows')
    pygame.display.update()


def end():
    # задание цикла для закрытия программы при нажатии кнопки
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                game_over = True


def image(link, pos=(500, 250)):
    # вставка изображения
    image = pygame.image.load(link)
    position_image = image.get_rect(center=(pos))
    screen.blit(image, position_image)
    pygame.display.update()


def title(text, size=40, font='calibri', color=(0, 0, 0), pos=(500, 150)):
    # вставка текста
    f = pygame.font.SysFont(font, size)
    t = f.render(text, True, color)
    position = t.get_rect(center=(pos))
    screen.blit(t, position)
    pygame.display.update()


def input(count):
    global screen
    global text_surface
    global user_number
    # основной шрифт для ввода
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    # создангие области ввода
    input_space = pygame.Rect(450, 200, 120, 32)
    active = True
    while active:
        for event in pygame.event.get():
            # закрытие окна
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # нажатие клавиши
            if event.type == pygame.KEYDOWN:
                # проверка на бэкспейс + стирание написанного
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
        user_number = copy.deepcopy(user_text)
        n = 0
        for i in user_number:
            if i == ' ':
                n += 1


        if len(user_text) == count:
            active = False
            user_text = ''
            # заливка области ввода
        color = pygame.Color(68, 148, 74)
        # добавление на экран области ввода
        pygame.draw.rect(screen, color, input_space)
        # рендер вводимого текста
        text_surface = base_font.render(user_text, True, (255, 238, 221))
        # фиксация области ввода + ее изменение в зав-ти от букв
        screen.blit(text_surface, (input_space.x + 5, input_space.y + 5))
        input_space.w = max(100, text_surface.get_width() + 10)
        pygame.display.update()
        pygame.display.flip()




# ________________________________________________________________
# ____________________________________________________________________func_end

run()

title('Добро пожаловать в игру Быки и Коровы!')

# _____________________ создание начального экрана
image('Images/Bull.png', pos=(600, 250))
image('Images/Cow.png', pos=(400, 250))

image_play = pygame.image.load('Images/play.png')
position_image_play = image_play.get_rect(center = (500, 350))
screen.blit(image_play,position_image_play)

image('Images/flower.png', pos=(950, 450))
image('Images/flower.png', pos=(950, 50))
image('Images/flower.png', pos=(50, 450))
image('Images/flower.png', pos=(50, 50))

# _____________________ начало игры по кнопке play
play = False
while not play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # нажатие на значок выхода
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pygame.mouse.get_rel()
    if pygame.mouse.get_focused() and position_image_play.collidepoint(pygame.mouse.get_pos()):
        btns = pygame.mouse.get_pressed()
        if btns[0]:
            run()
            play = True

# _____________________ генерирование числа компьютером
comp_number = []
while len(comp_number) < 4:
    a = random.randint(0, 9)
    if str(a) not in comp_number:
        comp_number.append(str(a))
title('Ваши попытки: ', size=20, pos=(900, 50))
print(comp_number)

# _____________________ цикл основного алгоритма игры
title('Введите четыре цифры через пробел:', size=30)
y = 80
play = True
while play == True:

    cow = 0; bull = 0
    input(7)
    user_number = str(user_number).split()

    k = 0
    for i in user_number:
        k = user_number.count(i) + k

    if k > 4:
        title('Число не может иметь одинаковые числа. Попробуйте еще раз ', size=30, pos=(500, 350))
        continue
    else:
        pygame.draw.rect(screen, (192, 220, 192), (90, 310, 900, 100))
    title(str(user_number), size=20, pos=(900, y))
    y += 20
    for n in range(4):
        if comp_number[n] == user_number[n]:
            bull += 1
        elif user_number[n] in comp_number:
            cow += 1
    base_font = pygame.font.Font(None, 32)
    cow_space = pygame.Rect(150, 200, 23, 32)
    bull_space = pygame.Rect(150, 250, 23, 32)
    color = pygame.Color(68, 148, 74)
    # вывод поля со значением коров
    image('Images/Cow.png', pos=(100, 225))
    pygame.draw.rect(screen, color, cow_space)
    text_surface = base_font.render(str(cow), True, (255, 238, 221))
    screen.blit(text_surface, (cow_space.x + 5, cow_space.y + 5))
    # вывод поля со значением быков
    image('Images/Bull.png', pos=(100, 275))
    pygame.draw.rect(screen, color, bull_space)
    text_surface = base_font.render(str(bull), True, (255, 238, 221))
    screen.blit(text_surface, (bull_space.x + 5, bull_space.y + 5))

    if bull == 4:
        run()
        image('Images/win.jpg', pos=(500, 175))
        title('Число угадано. Вы победили!', size=30, pos=(500, 350))

        play = False

pygame.display.update()
pygame.display.flip()

end()

