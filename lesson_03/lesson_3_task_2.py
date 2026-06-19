from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 17 Pro Max", "+79214561289"),
    Smartphone("Samsung", "Galaxy S26 Ultra", "+79157824410"),
    Smartphone("Xiaomi", "Xiaomi 15 Ultra",  "+79031156734"),
    Smartphone("Realme", "Realme GT 6", "+79648902345"),
    Smartphone("Google", "Google Pixel 10 Pro", "+79993417812")
]

for smartphone in catalog:
    print(f'{smartphone.brand} - {smartphone.model}. {smartphone.number}')







