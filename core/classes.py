from collections import namedtuple


class Car(namedtuple("Car", "brand model")):
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    pass


class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, cars):
        self.cars = cars

    def add(self, other):
        if isinstance(other, Car):
            self.cars.add(car)

    def delete(self, idx):
        if idx < len(self.cars):
            self.cars.pop(idx)

    def car_generator(self):
        for car in self.cars:
            yield car

    def __iter__(self):
        return self.car_generator()


if __name__ == '__main__':
    garage = Garage([Car("Fiat", "500"), Car("Toyota", "Corolla"), Car("Volvo", "S40")])
    for car in garage:
        print(car)
