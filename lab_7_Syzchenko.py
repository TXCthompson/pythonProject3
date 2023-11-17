###1################################################################

n = int(input("n?: "))
numbers = (2, 7, 1, 8, 5, 9, 3, 6, 4)

result = [q for q in numbers if q < n]
print(result)

###2################################################################

my_tuple = ('one', 'two', 'three')
print(', '.join(my_tuple))

###3################################################################

library = {
    'Книга1': {'Автор': 'Автор1', 'Рік видання': 2017, 'Кількість сторінок': 368},
    'Книга2': {'Автор': 'Автор2', 'Рік видання': 2005, 'Кількість сторінок': 224},
    'Книга3': {'Автор': 'Автор3', 'Рік видання': 2023, 'Кількість сторінок': 483},
}

book_title = input("Шановний, введіть назву книги: ")


if book_title in library:

    print(f"\nІнформація про книгу '{book_title}':")
    for key, value in library[book_title].items():
        print(f"{key}: {value}")
else:
    print(f"\nКниги з назвою '{book_title}' немає в бібліотеці.")

###4################################################################

students = {
    'Шевченко': ('Іван', 20, 'Інформатика'),
    'Петренко': ('Петро', 21, 'Економіка'),
    'Бондар': ('Микола', 19, 'Математика'),
}

student_lastname = input("Введіть прізвище студента: ")

if student_lastname in students:

    print(f"\nІнформація про студента {student_lastname}:")
    print(f"Ім'я: {students[student_lastname][0]}")
    print(f"Вік: {students[student_lastname][1]}")
    print(f"Спеціальність: {students[student_lastname][2]}")
else:
    print(f"\nСтудента із прізвищем '{student_lastname}' немає в словнику.")

###5################################################################

def add_phone_number(contacts, contact_name, new_phone_number):

    if contact_name in contacts:
        contacts[contact_name].append(new_phone_number)
        print(f"Новий номер телефону {new_phone_number} доданий для контакту {contact_name}.")
    else:
        print(f"Контакту {contact_name} немає в телефонній книзі.")


phone_book = {
    'Шевченко': ['+380-932-342-22-31', '+380-941-353-57-34'],
    'Петренко': ['+380-435-376-52-44'],
    'Бондар': ['+380-753-453-87-32', '+380-577-765-74-25'],
}

add_phone_number(phone_book, input('Введіть ім\'я: '), input('Введіть номер: '))

print("\nСписок номерів телефонів для всіх контактів:")
for contact, phone_numbers in phone_book.items():
    print(f"{contact}: {phone_numbers}")