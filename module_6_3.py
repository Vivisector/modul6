class Horse:

    def __init__(self, x_distance=0):
        self.x_distance = x_distance
        self.sound = '"Frrr"'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self, y_distance=0):
        self.y_distance = y_distance
        self.sound = '"I train, eat, sleep, and repeat"'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self, x_distance=0, y_distance=0):
        Horse.__init__(self, x_distance)
        Eagle.__init__(self, y_distance)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)

    def voice2(selfself):
        print(Horse().sound)



p1 = Pegasus()
print(Pegasus.mro())
print(f'\nПегас передвигается на 20 км по горизонтали и на 180 по вертикали')
p1.move(20, 180)
print(f'Пегас передвигается еще на 130 км по горизонтали и на 240 по вертикали')
p1.move(130, 240)
print(f'В результате на данный момент Пегас находится в координатах (x, y): {p1.get_pos()}')
print(f'При этом Пегас бормочет (как орёл, т.к. его голос перезаписался при Орловской инициализации, которая была последней):')
# print(p1.get_pos())

p1.voice()
print(f'Хотя скорее должен звучать как лошадь:')
p1.voice2()
# p1.fly(150)
# p1.fly(150)
# print(f'Пегас пробежал {p1.x_distance} км')
# print(f'Пегас пролетел {p1.y_distance} км')
