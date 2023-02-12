from typing import Union


class AirTransport:
    def __init__(self, volume_tank: Union[int, float], fuel_level: Union[int, float],
                 fuel_consumption: Union[int, float], range_of_flight: Union[int, float]):
        """
        Создание объекта класса 'Воздушное судно'
        :param volume_tank: объем топливного бака
        :param fuel_level:  текущий уровень топлива в баке
        :param fuel_consumption: потребление топлива в крейсерском режиме работы
        :param range_of_flight: дальность возможного полета
        """

        self._volume_tank = None
        self._init_volume_tank(volume_tank)  # для каждого объекта является константой - protect
        self._fuel_level = None
        self._init_fuel_level(fuel_level)  # не может изменяться вручную, только при совершении перелета или заправки - protect
        self._fuel_consumption = None
        self._init_fuel_consumption(fuel_consumption)  # для каждого объекта является константой - protect
        self._range_of_flight = None
        self._init_range_of_flight(range_of_flight)  # для каждого объекта является константой - protect

    def __str__(self) -> str:
        """
        Метод str
        :return: возвращает печатный вид экземпляра класса
        """
        return f"Воздушное судно имеет Объем бака:{self.volume_tank} литров;" \
               f"Содержит топлива:{self.fuel_level} литров; " \
               f"Потребляет топлива: {self.fuel_consumption} литров/час;" \
               f"Максимальная дальность полета: {self.range_of_flight} км"

    def __repr__(self) -> str:
        """
        Метод rerp
        :return: возвращает машинный вид экземпляра класса
        """
        return f"{self.__class__.__name__}(volume_tank={self.volume_tank}, " \
               f"fuel_level={self.fuel_level}, " \
               f"fuel_consumption={self.fuel_consumption}," \
               f"range_of_flight={self.range_of_flight})"

    def _init_volume_tank(self, volume_tank: Union[int, float]) -> None:
        """
        Создание защищенного атрибута
        :param volume_tank: объем топливного бака
        """
        if not isinstance(volume_tank, (int, float)):
            raise TypeError("Объем бака должен быть int или float")
        if not volume_tank > 0:
            raise ValueError("Объем бака должен быть положительным числом")
        self._volume_tank = volume_tank

    def _init_fuel_level(self, fuel_level: Union[int, float]) -> None:
        """
        Создание защищенного атрибута
        :param fuel_level: текущий уровень топлива в баке
        """
        if not isinstance(fuel_level, (int, float)):
            raise TypeError("Кол-во топлива должно быть int или float")
        if not fuel_level > 0:
            raise ValueError("Топливо дожно быть больше 0 ")
        self._fuel_level = fuel_level

    def _init_fuel_consumption(self, fuel_consumption: Union[int, float]) -> None:
        """
        Создание защищенного атрибута
        :param fuel_consumption: потребление топлива в крейсерском режиме работы
        """
        if not isinstance(fuel_consumption, (int, float)):
            raise TypeError("Потребление топлива должно быть int или float")
        if fuel_consumption < 0:
            raise ValueError("Потребление должно быть > 0")
        self._fuel_consumption = fuel_consumption

    def _init_range_of_flight(self, range_of_flight: Union[int, float]) -> None:
        """
        Создание защищенного атрибута
        :param range_of_flight: дальность возможного полета
        """
        if not isinstance(range_of_flight, (int, float)):
            raise TypeError("Дальность полета должна быть int или float")
        if not range_of_flight > 0:
            raise ValueError("Дальность полета не может быть меньше 0 ")
        self._range_of_flight = range_of_flight

    @property
    def volume_tank(self) -> Union[int, float]:
        """
        getter атрибута
        """
        return self._volume_tank

    @property
    def fuel_level(self) -> Union[int, float]:
        """
        getter атрибута
        """
        return self._fuel_level

    @property
    def fuel_consumption(self) -> Union[int, float]:
        """
        getter атрибута
        """
        return self._fuel_consumption

    @property
    def range_of_flight(self) -> Union[int, float]:
        """
        getter атрибута
        """
        return self._range_of_flight

    def refueling(self, fuel_amount_filled: Union[int, float]) -> None:
        """
        Метод заправки топлива в бак
        :param fuel_amount_filled: кол-во добаленного топлива
        """
        if not isinstance(fuel_amount_filled, (int, float)):
            raise TypeError("Кол-во заправленного топлива только int, float")
        if fuel_amount_filled < 0:
            raise ValueError("Нельзя заправить меньше 0 топлива")
        if fuel_amount_filled + self.fuel_level > self.volume_tank:
            raise ValueError("В бак столько топлива не влезет")
        self._fuel_level += fuel_amount_filled


class Airplane(AirTransport):
    def __init__(self, volume_tank: Union[int, float], fuel_level: Union[int, float],
                 fuel_consumption: Union[int, float], range_of_flight: Union[int, float],
                 takeoff_run: Union[int, float], passengers_places: Union[int]):
        """
        Класс самолет (Airplane) - дочерний для класса ВоздушныеСуда (AirTransport)
        :param volume_tank: объем топливного бака
        :param fuel_level:  текущий уровень топлива в баке
        :param fuel_consumption: потребление топлива в крейсерском режиме работы
        :param range_of_flight: дальность возможного полета
        :param takeoff_run: длина пробега - дистанция необходимая для взлета
        :param passengers_places: кол-во пассажирских мест
        """
        super().__init__(volume_tank, fuel_level, fuel_consumption, range_of_flight)
        self._takeoff_run = None  # для каждого объекта является константой - protect
        self._init_takeoff_run(takeoff_run)
        self._passengers_places = None  # для каждого объекта является константой - protect
        self._init_passengers_places(passengers_places)

    def __str__(self) -> str:
        """
        Перегрузка метода __str__
        :return: возвращает печатный вид экземпляра класса
        """
        return f"Самолет  имеет Объем бака:{self.volume_tank} литров; " \
               f"Содержит топлива:{self.fuel_level} литров; " \
               f"Потребляет топлива: {self.fuel_consumption} литров/час;" \
               f"Максимальная дальность полета: {self.range_of_flight} км; " \
               f"Расстояние пробега: {self.takeoff_run} м; " \
               f"Кол-во пассажиров: {self.passengers_places} чел-к."

    def __repr__(self) -> str:
        """
        Перегрузка метода __rerp__
        :return: возвращает машинный вид экземпляра класса
        """
        return f"{self.__class__.__name__}(volume_tank={self.volume_tank}, " \
               f"fuel_level={self.fuel_level}, " \
               f"fuel_consumption={self.fuel_consumption}," \
               f"range_of_flight={self.range_of_flight}), " \
               f"takeoff_run={self.takeoff_run}," \
               f"passengers_places={self.passengers_places}"

    def _init_takeoff_run(self, takeoff_run: Union[int, float]) -> None:
        """
        Создание защищенного атрибута
        :param takeoff_run: длина пробега - дистанция необходимая для взлета
        """
        if not isinstance(takeoff_run, (int, float)):
            raise TypeError("Длина пробега должна быть int или float")
        if takeoff_run < 0:
            raise ValueError("Длина пробега должна быть > 0")

        self._takeoff_run = takeoff_run

    def _init_passengers_places(self, passengers_places: Union[int]) -> None:
        """
        Создание защищенного атрибута
        :param passengers_places: кол-во пассажирских мест
        """
        if not isinstance(passengers_places, int):
            raise TypeError("Кол-во пассажирских мест должно быть только целым числом")
        if not passengers_places > 0:
            raise ValueError("Мест не может быть меньше 0")
        self._passengers_places = passengers_places

    @property
    def takeoff_run(self) -> Union[int, float]:
        """
        getter атрибута
        """
        return self._takeoff_run

    @property
    def passengers_places(self) -> Union[int]:
        """
        getter атрибута
        """
        return self._passengers_places

    def refueling(self, fuel_amount_filled: Union[int, float]) -> None:
        """
        Перегрузка метода базового класса
        Метод заправки топлива в бак
        :param fuel_amount_filled: кол-во добаленного топлива
        """
        if not isinstance(fuel_amount_filled, (int, float)):
            raise TypeError("Кол-во заправленного топлива только int, float")
        if fuel_amount_filled < 0:
            raise ValueError("Нельзя заправить меньше 0 топлива")
        if fuel_amount_filled + self.fuel_level > self.volume_tank:
            raise ValueError("В бак столько топлива не влезет")
        self._fuel_level += fuel_amount_filled


class Helicopter(AirTransport):
    def __init__(self, volume_tank: Union[int, float], fuel_level: Union[int, float],
                 fuel_consumption: Union[int, float], range_of_flight: Union[int, float],
                 load_capacity: Union[int, float]):
        """
        Класс вертолет (Helicopter) - дочерний для класса ВоздушныеСуда (AirTransport)
        :param volume_tank: объем топливного бака
        :param fuel_level:  текущий уровень топлива в баке
        :param fuel_consumption: потребление топлива в крейсерском режиме работы
        :param range_of_flight: дальность возможного полета
        :param load_capacity: грузоподъемность
        """
        super().__init__(volume_tank, fuel_level, fuel_consumption, range_of_flight)
        self._load_capacity = None  # для каждого объекта является константой - protect
        self._init_load_capacity(load_capacity)

    def __str__(self) -> str:
        """
        Перегрузка метода __str__
        :return: возвращает печатный вид экземпляра класса
        """
        return f"Вертолет имеет Объем бака:{self.volume_tank} литров; " \
               f"Содержит топлива:{self.fuel_level} литров; " \
               f"Потребляет топлива: {self.fuel_consumption} литров/час;" \
               f"Максимальная дальность полета: {self.range_of_flight} км; " \
               f"грузоподъемность: {self.load_capacity} кг; "

    def __repr__(self) -> str:
        """
        Перегрузка метода __rerp__
        :return: возвращает машинный вид экземпляра класса
        """
        return f"{self.__class__.__name__}(volume_tank={self.volume_tank}, " \
               f"fuel_level={self.fuel_level}, " \
               f"fuel_consumption={self.fuel_consumption}," \
               f"range_of_flight={self.range_of_flight}), " \
               f"load_capacity={self.load_capacity}"

    def _init_load_capacity(self, load_capacity: Union[int, float]) -> None:
        """
        Создание защищенного атрибута
        :param load_capacity: грузоподъемность
        """
        if not isinstance(load_capacity, (int, float)):
            raise TypeError("Грузоподъемность должна быть int или float")
        if not load_capacity > 0:
            raise ValueError("Грузоподъемность не может быть < 0")

        self._load_capacity = load_capacity

    @property
    def load_capacity(self) -> Union[int, float]:
        """
        getter атрибута
        """
        return self._load_capacity

    def refueling(self, fuel_amount_filled: Union[int, float]) -> None:
        """
        Перегрузка метода базового класса
        Метод заправки топлива в бак
        :param fuel_amount_filled: кол-во добаленного топлива
        """
        if not isinstance(fuel_amount_filled, (int, float)):
            raise TypeError("Кол-во заправленного топлива только int, float")
        if fuel_amount_filled < 0:
            raise ValueError("Нельзя заправить меньше 0 топлива")
        if fuel_amount_filled + self.fuel_level > self.volume_tank:
            raise ValueError("В бак столько топлива не влезет")
        self._fuel_level += fuel_amount_filled
