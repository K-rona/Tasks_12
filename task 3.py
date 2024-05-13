class Meeting:
    lst_meeting = []

    def __init__(self, id, date, title):
        self.id = id
        self.date = date
        self.title = title
        self.employees = []
        Meeting.lst_meeting.append(self)

    def add_person(self, person):
        self.employees.append(person)

    def count(self):
        return len(self.employees)

    @classmethod
    def total(cls):
        count = 0
        for meeting in cls.lst_meeting:
            count += len(meeting.employees)
        return count

    @classmethod
    def count_meeting(cls, date):
        count = 0
        for meeting in cls.lst_meeting:
            if str(meeting.date) == str(date):
                count += 1
        return count

    def __repr__(self):
        result = f'Рабочая встреча {self.id}\n' \
               f'{self.date} {self.title}\n'
        for employee in self.employees:
            result += str(employee) + '\n'
        return result


class User:
    People = []

    def __init__(self, id, nick_name, first_name, last_name, middle_name, gender):
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender
        User.People.append(self)

    def __repr__(self):
        if len(self.gender) > 0:
            return f'ID: {self.id} LOGIN:{self.nick_name} NAME:{self.last_name} {self.first_name} {self.middle_name} ' \
                   f'GENDER:{self.gender}'
        return f'ID: {self.id} LOGIN:{self.nick_name} NAME:{self.last_name} {self.first_name} {self.middle_name}'


class Date:
    month = {
        1: 'янв',
        2: 'фев',
        3: 'мар',
        4: 'апр',
        5: 'май',
        6: 'июн',
        7: 'июл',
        8: 'авг',
        9: 'сен',
        10: 'окт',
        11: 'ноя',
        12: 'дек'
    }

    def __init__(self, date: str):
        self.day = date[:2]
        self.month = Date.month[int(date[3:5])]
        self.year = date[6:]

    def __repr__(self):
        return f'{self.day} {self.month} {self.year} г.'


class Load:

    @staticmethod
    def write(name_1, name_2, name_3):
        with open(f'{name_1}', 'r', encoding='utf8') as f:
            info = f.readlines()
        info = info[1:]
        for line in info:
            id, date, title = line.rstrip()[:-1].split(";")
            new_meeting = Meeting(id, Date(date), title)

        with open(f'{name_2}', 'r', encoding='utf8') as f:
            info = f.readlines()
        info = info[1:]
        for line in info:
            id, nick_name, first_name, last_name, middle_name, gender = line.rstrip()[:-1].split(";")
            new_person = User(id, nick_name, first_name, last_name, middle_name, gender)

        with open(f'{name_3}', 'r', encoding='utf8') as f:
            info = f.readlines()
        info = info[1:]
        for line in info:
            id_meet, id_pers = line.rstrip()[:-1].split(";")
            for person in User.People:
                if person.id == id_pers:
                    for meeting in Meeting.lst_meeting:
                        if meeting.id == id_meet:
                            meeting.add_person(person)


Load.write('meetings.txt', 'persons.txt', 'pers_meetings.txt')
for item in Meeting.lst_meeting:
    print(item)
print(Meeting.total())
print(Meeting.count_meeting(Date('21.04.2020')))

