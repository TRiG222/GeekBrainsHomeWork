def get_contact(name, surname, birth, city, phone, email):
    print(f'Вас зовут {name.title()} {surname.title()}, родились {birth} в городе {city.title()}, ваши контакты: {phone} {email}')


get_contact(
    name=input('Как вас зовут? '),
    surname=input('Ваша фамилия? '),
    birth=input('Дата вашего рождения? '),
    city=input('Город вашего рождения? '),
    phone=input('Ваш номер? '),
    email=input('Ваш email? '))
