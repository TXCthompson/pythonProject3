import math

###1######################################################

def g_function(x, mu, sigma):
    exp = -((x - mu) ** 2) / (2 * sigma ** 2)
    coeff = 1 / (math.sqrt(2 * math.pi) * sigma)
    res = coeff * math.exp(exp)
    return res

mu = 0
sigma = 1

x = input("Введіть значення 'X': ")
g_value = g_function(float(x), mu, sigma)

print(f'Значення функції Гауса для X = {x}: {g_value}')

###2#######################################################

john = 3
mary = 5
adam = 6

totalApples = john + mary + adam

print(john, mary, adam, sep=', ')
print(f'Загальна кількість яблук: {totalApples}')

###3#######################################################

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

###4#######################################################

x = input()
x = float(x)
y = ((x ** 3) * 3) - ((x ** 2) * 2) + (3 ** x) - 1
print("y =", y)

###5#######################################################

# this program computes the number of seconds in a given number of hours

hours = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours: ", hours) # printing the number of hours

###6#######################################################

a = float(input('Введіть перше число: '))
b = float(input('Введіть друге число: '))

print(f'Результат додавання {a} + {b} = {a + b}')
print(f'Результат віднімання {a} - {b} = {a - b}')
print(f'Результат множення {a} * {b} = {a * b}')
if (b == 0):
    print(f'Вибачте, на нуль ділити неможливо!')
else:
    print(f'Результат ділення {a} / {b} = {a / b}')

print("\nThat's all, folks!")

###7#######################################################

x = float(input("Enter value for x: "))

y = 1 / (x + 1 / (x + 1 / (x + 1 / (x + (1 / x)))))

print("y =", y)

###8#######################################################

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

def func_time(hour, mins, dura):
    if (mins + dura < 60):
        mins += dura
        return print(f'{hour}:{mins}') if mins > 9 else print(f'{hour}:0{mins}')
    else:
        hour += 1
        mins -= 60
        if hour > 23:
             hour -= 24
        func_time(hour, mins, dura)

func_time(hour, mins, dura)