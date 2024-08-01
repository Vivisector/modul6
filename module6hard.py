import math

class Figure:
    _SIDES = None

    def __init__(self, color=(), *sides, filled=True):
        self.__color = color
        # self.__sides = list(sides)
        self.filled = filled

        if not self.__is_valid_sides(sides):
            # print(f"Задано некорректное количество сторон: {len(list(*sides))}.")
            # print(len(list(sides)))
            if len(list(sides)) == self._SIDES or len(list(sides)) == 1 or len(list(sides)) == 12:
                self.__sides = sides[0] * self._SIDES
            else:
                self.__sides = [1] * self._SIDES
        else:
            self.__sides = list(sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, color):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in color)

    def set_color(self, *color):
        color_src = self.get_color()  # Сохраняем текущий цвет
        # print(f"Текущий цвет до изменения: {color_src}")

        if self.__is_valid_color(color):
            self.__color = color
        else:
            print(f'Задан недопустимый цвет {color}. Остается прежним:')

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *sides):
        if len(sides) != self._SIDES:  # and len(sides) != 1:
            return False
        return True

    def set_sides(self, *new_sides):
        # print(self.__sides)
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        elif len(new_sides) == 1:
            if self._SIDES == 1:
                self.__sides = list(new_sides)
            elif self._SIDES == 12:
                pass
            else:
                self.__sides = [new_sides[0]] * self._SIDES
        else:
            if len(self.__sides) == 1:
                self.__sides = [new_sides[0]] * self._SIDES
            else:
                pass

    def __len__(self):
        # Проверка, что внутри self.__sides находится кортеж с одним элементом
        if len(self.__sides) == 1 and isinstance(self.__sides[0], tuple):
            # Возвращаем первый элемент внутреннего кортежа
            return self.__sides[0][0]
        else:
            return sum(self.__sides)

    def isfilled(self):
        return self.filled


class Circle(Figure):
    _SIDES = 1

    def __init__(self, color=(), *sides, filled=True):
        super().__init__(color, sides, filled=filled)  # Вызов конструктора базового класса
        # self._SIDES = 1

    def get_radius(self):
        perimetr = self.__len__()
        return perimetr / (2 * math.pi)

    def get_square(self):
        return math.pi * self.get_radius() * self.get_radius()


class Triangle(Figure):
    _SIDES = 3

    def __init__(self, color=(), *sides, filled=True):
        super().__init__(color, 3, filled=filled)
        # self._SIDES = 3


class Cube(Figure):
    _SIDES = 12

    def __init__(self, color=(), *sides, filled=True):
        super().__init__(color, sides, filled=filled)

    def get_volume(self):
        side = self.get_sides()
        return side[0] ** 3


###### проверки ######
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(f'После изменения цветов на 55, 66, 77 цвет стал как и задавали: {circle1.get_color()}')
cube1.set_color(300, 70, 15)  # Не изменится
# print(f'После попытки изменения цветов на 300, 70, 15 цвет остался прежним:')#{cube1.get_color()}')
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
# print(cube1.get_sides())
print(list(cube1.get_sides()))
circle1.set_sides(15)  # Изменится
print(f'Получаем длину окружности круга {circle1.get_sides()}')

# Проверка периметра (круга), это и есть длина:
print(f'Длина окружности равна переданному параметру {len(circle1)}')

# Проверка объёма (куба):
print(f'Объем куба: {cube1.get_volume()}')

circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
print(f'Длина окружности равна переданному параметру {len(circle1)}')
print(f'Радиус окружности с длиной стороны {circle1.__len__()} - {round(circle1.get_radius(), 2)} ед.')
print(f'Площадь окружности с длиной стороны {circle1.__len__()} - {round(circle1.get_square(), 2)} ед.')
