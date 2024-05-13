class AirTicket:

    def __init__(self, name, _from, to, date_time, flight, seat, _class, gate):
        self.passenger_name = name
        self._from = _from
        self.to = to
        self.date_time = date_time
        self.flight = flight
        self.seat = seat
        self._class = _class
        self.gate = gate

    def __repr__(self):
       return f'|{self.passenger_name:<16}|{self._from} |{self.to}|'\
              f'{self.date_time}|{self.flight:<20}|' \
              f'{self.seat:<4}|{self._class:<2}|' \
              f'{self.gate:<4}|'


class Load:
    data = []

    @staticmethod
    def write(file_name):

        with open(f'{file_name}', 'r', encoding='utf8') as f:
            info = f.readlines()
        info = info[1:]
        for line in info:
            name, _from, to, data_time, flight, seat, _class, gate = line.rstrip()[:-1].split(";")
            new_ticket = AirTicket(name, _from, to, data_time, flight, seat, _class, gate)
            Load.data.append(new_ticket)


tickets = Load.write('tickets.txt')
print('-' * 79)
print('|     NAME       |FROM|TO |   DATE/TIME    |       FLIGHT       |SEAT|CLS|GATE|')
print('=' * 79)
for item in Load.data:
    print(item)
print('-' * 79)
