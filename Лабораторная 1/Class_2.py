import doctest


class Staff:
    def __init__(self, number_of_persons: int, tax_rate: int, number_of_departments: int):
        """

        :param number_of_persons: кол-во сотрудников в организации
        :param tax_rate: налоговая ставка предприятия
        :param number_of_departments: количество отделов
        Примеры:
        >>> roga_koputa = Staff(10, 13, 1)  # инициализация экземпляра класса
        """
        self.number_of_persons = number_of_persons
        self.tax_rate = tax_rate
        self.number_of_departments = number_of_departments

        if not isinstance(number_of_departments, int):
            raise TypeError("Сотрудников должно быть целое колличество")
        if tax_rate < 5:
            raise ValueError("Налоговая ставка не может быть ниже 5%")
        if number_of_persons < 1:
            raise ValueError("В компании не может быть меньше 1 человека")
        if number_of_departments < 1:
            raise ValueError("Должен быть хотя бы один отдел")



    def registration_of_new_employee (self, name: str, age: int, working_rate: (int, float)) -> str: #Если реализовывать метод, то получим сообшщение "Новый сотрудник принят"
        """
        Прием на работу новго сотрудника
        :param name: Имя принимаемого сотрудника
        :param age: Возвраст
        :param working_rate: Ставка на которую оформляют сотрудника
        :return: Сообщение что сотрудник принят на работу
        """
        if not isinstance(name, str):
            raise TypeError("Имя может быть только str")
        if age < 18:
            raise ValueError("Младше 14 лет официально трудоустроить человека нельзя")
        if working_rate < 0.5:
            raise ValueError("Минимальная ставка 0.5")


    # Начисление зарплаты
    def payroll (self, worked_hours: int, working_rate: (float, int)) -> (int, float):
        """
        Начисление зарплаты
        :param worked_hours: отработано часов
        :param working_rate: ставка на которую оформлен человек
        :return: зарплата
        """

        if worked_hours <= 0:
            raise ValueError("В этом месяце ЗП не положена, так как человек не работал")



    # Увольнение
    def dismissal_of_an_employee (self, name, cause) -> str:
        """
        Увольнение сотрудника
        :param name: Имя
        :param cause: Причина
        :return: Сообщение об увольнении с причиной
        """

        if name is None:
            raise ValueError("Нужно указать имя кого увольняем")
        if cause is None:
            raise ValueError("Без причины увольнять нельзя")

if __name__ == "__main__":
     doctest.testmod()

roga_koputa = Staff(10, 13, 1) #Создаем экземпляр класса
print(roga_koputa.tax_rate)
