def get_contact_data(name, surname, age, city, email, phone):
    return f'имя: {name}, фамилия: {surname}, возраст: {age}, город: {city}, емайл: {email}, телефон: {phone}'


print(get_contact_data(name='Иван'
                       , surname='Иванов'
                       , age='100'
                       , city='Бобруйск'
                       , email='Ivan@mail.ru'
                       , phone='123456789'))
