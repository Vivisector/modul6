# class Human:
#     head = True
#
#     # def __init__(self):
#     #     self.about()
#
#     def say_hellow(self):
#         print('Здравствуйте!')
#
# class Student(Human):
#     head = False
#
#     def about(self):
#         print('Я студент')
#
# class Teacher(Human):
#     pass
#
# # st0 = Human()
# st1 = Student()
# t1 = Teacher()
# print(st1.head)
# # st1.say_hellow()
# print('Говорит учитель')
# t1.say_hellow()
# print('Говорит студент')
# st1.say_hellow()
#
# exit()
class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):
        if food.edible:
            self.fed = True
            # print(f'{self.name} съел {food.name} и жив? {self.alive}')
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            # print(f'{self.name} не стал есть {food.name} и накормлен? {self.fed}')
            # или
            print(f'{self.name} съел несъедобный {food.name}')

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)



class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)



class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        # self.edible = False

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(f'Первое животное: {a1.name}')
print(f'Первое растение: {p1.name}\n')
# print(f'Съедобность "{p1.name}": {p1.edible}')
# print(f'Съедобность "{p2.name}": {p2.edible}')

# print(a1.alive)
# print(a2.fed)
print(f'{a1.name} жив? (до еды) {a1.alive}')
print(f'{a2.name} жив? (до еды) {a2.alive}\n')
a1.eat(p1)
print(f'{a1.name} жив? - {a1.alive}')
print(f'потому что "{p1.name}" съедобен? {p1.edible}\n')
a2.eat(p2)
print(f'{a2.name} жив? - {a2.fed}')
print(f'потому что "{p2.name}" съедобен? {p2.edible}')