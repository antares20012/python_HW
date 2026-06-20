from address import Address

from mailing import Mailing


# 1. Создаем адрес получателя и адрес отправителя
sender = Address("658076", "Сибирский", "Кедровая", "17", "32")
receiver = Address("143007", "Одинцово", "Маршала Жукова", "12", "45")

# 2. Создаем один экземпляр Mailing, передавая в него адреса
mailing = Mailing(from_address=sender, to_address=receiver, cost = 12342324.22, track= "sdfgkjhvvsdkj")

# 3. Получаем и печатаем ВСЕ данные только из экземпляра shipment
print(f'Отправление {mailing.track} из {sender.index}, {sender.city}, {sender.street_name}, {sender.building} - {sender.apartment_number} '
      f'в {receiver.index}, {receiver.city}, {receiver.street_name}, {receiver.building} - {receiver.apartment_number}. '
      f'Стоимость {mailing.cost} рублей')


