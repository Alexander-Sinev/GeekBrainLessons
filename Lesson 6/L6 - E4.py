class Car:
    # atr
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


Mustang = SportCar(100, 'Red', 'Mustang', False)
BMW = TownCar(30, 'White', 'BMW', False)
LandRover = WorkCar(70, 'Black', 'LandRover', True)
ford = PoliceCar(110, 'Blue',  'Ford', True)
print(LandRover.turn_left())
print(f'When {BMW.turn_right()}, then {Mustang.stop()}')
print(f'{LandRover.go()} with speed exactly {LandRover.show_speed()}')
print(f'{LandRover.name} is {LandRover.color}')
print(f'Is {Mustang.name} a police car? {Mustang.is_police}')
print(f'Is {LandRover.name}  a police car? {LandRover.is_police}')
print(Mustang.show_speed())
print(BMW.show_speed())
print(ford.police())
print(ford.show_speed())
