from address import Address


class Mailing:
    def __init__(self, to_address: Address, from_address: Address, cost: float, track: str):
        self.to_address = to_address        #Адрес получателя
        self.from_address = from_address    #Адрес отправителя
        self.cost = cost                    #Стоимость
        self.track = track                  #Трек номер

    def addAddress(self, address: Address):
        self.to_address = address
        self.from_address = address
        