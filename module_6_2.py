class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        # print(self.get_model())
        # print(self.get_horsepower())
        # print(self.get_color())
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец ТС: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Цвет {new_color} не предусмотрен в текущей комплектации')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    # def __init__(self):
    #     self.__PASSENGERS_LIMIT


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
print()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
print('\nДоступ к приватному атрибуту "__model"')
# print(vehicle1.__model)
print(vehicle1._Vehicle__model)