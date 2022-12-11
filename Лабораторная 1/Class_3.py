import doctest


class Sklad:

    def __init__(self, warehouse_number: int, products: str, length: int, width: int, number_of_racks: int):
        """

        :param warehouse_number: Номер склада
        :param products: Тип хранимой продукции
        :param length: Длина склада
        :param width: Ширина склада
        :param number_of_racks: Количество стелажей
        Пример:
        >>>siniy_sklad = Sklad(1, "Бананы", 100, 100, 5) #Инициализация экземпляра
        """
        self.warehouse_number = warehouse_number
        self.products = products
        self.length = length
        self.width = width
        self.number_of_racks = number_of_racks

        if not isinstance(warehouse_number, int):
            raise TypeError("Номер склада может быть только целым числом")
        if warehouse_number <= 0:
            raise ValueError("Склад должен быть целым числом больше 0")
        if not isinstance(width, int):
            raise TypeError("Ширина склада может быть только целым числом")
        if not isinstance(length, int):
            raise TypeError("Длина склада может быть только целым числом")



    def how_much_can_we_load(self, racks_area: (int, float)) -> int:
        """
        Сколько можно загрузить стелажей
        :param racks_area: Площадь одного стелажа
        :return: количество стелажей, которые можем погрузить
        """
        area = self.width * self.length
        racks_load_numb = area / racks_area
        return racks_load_numb

        if racks_area > area:
            raise ValueError("Площадь стелажа не может быть больше площади склада")
        if not isinstance(racks_load_numb, int, float):
            raise TypeError("Только числовое значение")

    # Поступление продукции
    def product_receipt(self, how_many_products_were_received: (int, float)) -> str:
        """
        Метод приема новго товара на склад
        :param how_many_products_were_received: сколько приехало товара
        :return: Сообщение о приеме товара на self.warehouse_number
        """

        if how_many_products_were_received <= 0:
            raise ValueError("Количество продукции не может быть <=0")
        if not isinstance(how_many_products_were_received, int, float):
            raise TypeError("Введите количество товара")

if __name__ == "__main__":
     doctest.testmod()
