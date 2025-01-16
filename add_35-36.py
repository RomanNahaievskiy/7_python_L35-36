'''
!!! Обов'язкова умова
Результат обчислення
площі у вашому коді зберегти в змінній area
area =
'''

# Ваш код тут (змінюй рядки нижче)
......
......
area = ....

# Частина надана Gen`ом (не змінюй рядки нижче)
try:
    # Перевірка, чи area визначена як число
    if isinstance(area, (int, float)):
        if area > 0:  # Перевірка, чи area більше за нуль
            if area < 50:
                print("Gen, цей стіл занадто малий для навчання.")
                print("Сподіваюсь тобі вистачає місця.")
            elif area > 150:
                print("Gen, Ого цей стіл досить великий!")
            else:
                print("Gen, твій стіл чудово підходить для навчання!")
        else:
            print("Gen: Помилка!")
            print("Площа не може бути нульовою або від'ємною.")
    else:
        raise TypeError  # Якщо area не є числом, викликати помилку
except NameError:
    print("Gen: Помилка!")
    print("Змінна area не визначена, або хтось забув про типи даних.")
except TypeError:
    print("Gen: Помилка!")
    print("Значення змінної area некоректне. Очікується число.")