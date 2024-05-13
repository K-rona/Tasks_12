class Date:
    month = {1: ["янв", 31, 31],
             2: ["фев", 28, 29],
             3: ["мар", 31, 31],
             4: ["апр", 30, 30],
             5: ["май", 31, 31],
             6: ["июн", 30, 30],
             7: ["июл", 31, 31],
             8: ["авг", 31, 31],
             9: ["сен", 30, 30],
             10: ["окт", 31, 31],
             11: ["ноя", 30, 30],
             12: ["дек", 31, 31]
             }

    def __init__(self, date: str):
        if Date.data_check(date):
            self.__date = date
        else:
            print("Value Error")
            self.__date = None

    @staticmethod
    def data_check(value: str):
        if len(value) == 10:
            if 1970 <= int(value[6:10]) <= 2024:
                if int(value[3:5]) in Date.month:
                    if Date.leap_year(int(value[6:10])):
                        if 0 <= int(value[:2]) <= Date.month[int(value[3:5])][2]:
                            return True
                    else:
                        if 0 <= int(value[:2]) <= Date.month[int(value[3:5])][1]:
                            return True

        else:
            return False

    @staticmethod
    def leap_year(value: int):
        if value % 4 != 0:
            return False
        elif value % 100 == 0:
            if value % 400 == 0:
                return True
            else:
                return False
        return True

    date = property()

    @date.setter
    def date(self, value):
        if Date.data_check(value):
            self.__date = value
        else:
            print("Value Error")

    @date.getter
    def date(self):
        string = self.__date
        if string is None:
            return "None"
        day = int(string[:2])
        month = Date.month[int(string[3:5])][0]
        year = string[6:10]
        return f'{day} {month} {year} г.'

    def __repr__(self):
        string = self.__date
        if string is None:
            return "None"
        day = int(string[:2])
        month = Date.month[int(string[3:5])][0]
        year = string[6:10]
        return f'{day} {month} {year} г.'

    def to_timestamp(self):
        string = self.__date
        day = int(string[:2])
        month = int(string[3:5])
        year = int(string[6:10])
        result = 0
        result += day - 1
        if Date.leap_year(year):
            for i in range(1, month):
                result += Date.month[i][2]
        else:
            for i in range(1, month):
                result += Date.month[i][1]

        for j in range(1970, year):
            if Date.leap_year(j):
                result += 366
            else:
                result += 365

        return result * 24 * 3600

    def __lt__(self, other):
        if self.__date is None or other.__date is None:
            return "Error"
        if self.to_timestamp() >= other.to_timestamp():
            return False
        return True

    def __le__(self, other):
        if self.__date is None or other.__date is None:
            return "Error"
        if self.to_timestamp() > other.to_timestamp():
            return False
        return True

    def __gt__(self, other):
        if self.__date is None or other.__date is None:
            return "Error"
        if self.to_timestamp() <= other.to_timestamp():
            return False
        return True

    def __ge__(self, other):
        if self.__date is None or other.__date is None:
            return "Error"
        if self.to_timestamp() < other.to_timestamp():
            return False
        return True

    def __eq__(self, other):
        if self.__date is None or other.__date is None:
            return "Error"
        for i in self.__date:
            for j in other.__date:
                if i == j:
                    continue
                else:
                    return False
            return True

    def __ne__(self, other):
        if self.__date is None or other.date is None:
            return "Error"
        for i in self.__date:
            for j in other.date:
                if i != j:
                    return True
        return False


d1 = Date('07.12.2021')
print(d1.date)
d1.date = '14.02.2022'
print(d1.date)
print(d1.to_timestamp())
d2 = Date('32.14.2020')
print(d2.date)
d2.date = '29.02.2021'
print(d2)
d2.date = '29.02.2020'
print(d2.date)
if d1 < d2:
    print('YES')
else:
    print('NO')
print(d1 >= d2)
print(d1 != Date('01.01.2023'))
print(d1 <= d2)