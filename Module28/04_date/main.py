import time


class Date:
    """ Класс даты, который инициируется по строковой записи даты """
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def is_date_valid(cls, date_string: str) -> bool:
        """ Проверяет правильность даты """
        try:
            time.strptime(date_string, "%d-%m-%Y")
            return True
        except ValueError:
            return False

    @classmethod
    def from_string(cls, date_string: str) -> "Date":
        """ Возвращает класс из строкового представления даты """
        if cls.is_date_valid(date_string):
            extracted_date = time.strptime(date_string, "%d-%m-%Y")
            return cls(year=extracted_date.tm_year, month=extracted_date.tm_mon, day=extracted_date.tm_mday)

    def __str__(self) -> str:
        return f"День: {self.day}\tМесяц: {self.month}\tГод: {self.year}"


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
