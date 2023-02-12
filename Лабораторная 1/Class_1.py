import doctest


class Car:

    def __init__(self, brand: str, volume_of_the_tank: int, mileage: (int, float), fuel_quantity: (int, float), tires: str):
        """
        Сорздание машины
        :param brand: Марка машины
        :param volume_of_the_tank: Объем топливного бака
        :param mileage: Пробег автомобиля
        :param fuel_quantity: Количество топлива в машине
        :param tires: Тип резины
        Примеры:
        >>> car_2 = Car("ВАЗ", 40, 1000, 30, "Зимняя")  # инициализация экземпляра класса
        """

        self.brand = brand
        self.volume_of_the_tank = volume_of_the_tank
        self.mileage = mileage
        self.fuel_quantity = fuel_quantity
        self.tires = tires
        if not isinstance(brand, str):
            raise TypeError("Название бренда должно быть str")
        if volume_of_the_tank <= 0:
            raise ValueError("Объем бака должен быть больше 0")
        if mileage <= 0:
            raise ValueError("Пробег должен быть больше 0")
        if fuel_quantity <= 0:
            raise ValueError("Без топлива машина не ездит!")
        if volume_of_the_tank < fuel_quantity:
            raise ValueError("Топлива не может быть больше чем объем бака")

    def increase_in_mileage (self, passed_distance: int) -> None:
        """
        Увеличение пробега
        :param passed_distance: Пройденная дистанция
        :return: Новый пробег автомобиля
        """
        self.mileage += passed_distance

        if self.mileage < self.mileage:
            raise ValueError("Пробег нельзя уменьшать")


    def car_refueling (self, poured_fuel: (float, int)) -> None:
        """
        Метод добавления топлива в бак автомобиля
        :param poured_fuel: сколько топлива заправили
        :return: количество топлива в баке
        """
        self.fuel_quantity += poured_fuel

        if self.fuel_quantity + poured_fuel > self.volume_of_the_tank:
            raise ValueError("Столько заправить невозможно, так как объем бака меньше")


    def tire_replacement (self, tire_type: str, season: str) -> None:
        """
        Смена резины на автомобиле
        :param tire_type: тип резины установленой сейчас
        :param season: какое сейчас время года, если  температура выше 0 - Лето, если ниже - Зима
        :return: новый тип резины на машине
        """

        if self.tires == "Зимние" and season == "Лето":
            raise ValueError("Нужно сменить покрышки!")


if __name__ == "__main__":
    doctest.testmod()
