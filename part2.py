#-----------------------------Цикли-----------------------------------

#If/Else
num = 15  # приклад значення для num

if num > 10:
    print("num більше за 10")
else:
    print("num не більше за 10")

#-----------------------------
#If-Elif-Else
a = input('Введіть число')
a = int(a)
if a > 0:
    print('Число додатне')
elif a < 0:
    print("Число від'ємне")
else:
    print('Це число - нуль')


#-----------------------------
#is (перевіряє чи два об'єкти вказують на одну і ту ж область пам'яті)
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  # True
print(a is c)  # False

#перевірка чи є змінна None
if my_var is None:
    pass # Робимо щось, якщо 'my_var' є 'None'

#-----------------------------
#AND, OR, NOT

#AND - True якщо дві істини
#OR - True якщо хоча б одна з умов істина
#NOT - інвертує значення (True-False, False-True)
num = int(input("Введіть число: "))
length = len(str(num)) #перетворює число в рядок і обчислює його довжину
if length == 2 and num % 2 == 0: #переваіряємо довжину числа та на парність
    print("Парне двозначне число")
else:
    print("Ні")


a = not 2 < 0  # True

#Задача "FizzBuzz”
#Виводить "Fizz", якщо число кратне якомусь певному числу (наприклад, 3);
#Виводить "Buzz", якщо число кратне іншому певному числу (наприклад, 5);
#Виводить "FizzBuzz", якщо число кратне обом цим числам;
#В іншому випадку виводить саме число.

# Задаємо конкретне число
num = int(input())

# Перевіряємо кратність
if num % 3 == 0 and num % 5 == 0: #спочатку найспецефічніша перевірка
    print("FizzBuzz")
elif num % 3 == 0: #після цієї або перевірки з 5, перевірка з умовою and не була б виконана
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)


#-----------------------------
#Блоки
if x >= 0:
    if y >= 0:  # x > 0, y > 0
        print("Перша чверть")
    else:  # x > 0, y < 0
        print("Четверта чверть")
else:
    if y >= 0:  # x < 0, y > 0
        print("Друга чверть")
    else:  # x < 0, y < 0
        print("Третя чверть")

#Тернарні операції
is_nice = True
state = "nice" if is_nice else "not nice"
#АБО
is_nice = True
if is_nice:
    state = "nice"
else:
    state = "not nice"

#з використанням OR
some_data = None
msg = some_data or "Не було повернено даних"
#АБО з використанням Else/If
some_data = None
if some_data:
    msg = some_data
else:
    msg = "Не було повернено даних"


#Match
fruit = "apple"
match fruit:
    case "apple":
        print("This is an apple.")
    case "banana":
        print("This is a banana.")
    case "orange":
        print("This is an orange.")
    case _: #символ для вказівки на будь-які інші випадки
        print("Unknown fruit.")

#З використанням змінних у шаблонах
point = (1, 0)

match point:
    case (0, 0):
        print("Точка в центрі координат")  
    case (0, y):
        print(f"Точка лежить на осі Y: y={y}")  
    case (x, 0):
        print(f"Точка лежить на осі X: x={x}") 
    case (x, y):
        print(f"Точка має координати:  x={x}, y={y}") 
    case _:
        print("Це не точка")

#З колекціями
pets = ["dog", "fish", "cat"]

match pets:
    case ["dog", "cat", _]:
        # Випадок, коли є і собака, і кіт
        print("There's a dog and a cat.")
    case ["dog", _, _]:
        # Випадок, коли є тільки собака
        print("There's a dog.")
    case _:
        # Випадок для інших комбінацій
        print("No dogs.")


#-----------------------------
#Цикли

#For - ітерація по елементах будь-якої послідовності
#While - виконує блок коду, поки задана умова є істинною (True)

#For
fruit = 'apple'
for char in fruit:
    print(char)

some_iterable = ["a", "b", "c"]
for i in some_iterable:
    print(i)

#Задача підрахувати кіл-ть пробілів та символів в рядку.
# Зчитування рядка від користувача
user_input = input("Введіть рядок: ")

# Ініціалізація змінних для підрахунку символів та пробілів
total_chars = len(user_input)  # загальна кількість символів у рядку
space_count = 0  # кількість пробілів

# Підрахунок кількості пробілів
for char in user_input:
    if char == " ":
        space_count += 1

# Виведення результатів
print(f"Загальна кількість символів у рядку: {total_chars}")
print(f"Кількість пробілів у рядку: {space_count}")

#-------------
# Функція Range 
# - створює послідовність чисел
# range(stop): Створює послідовність чисел від 0 до stop - 1.
# range(start, stop): Генерує числа від start до stop - 1.
# range(start, stop, step): Створює числа від start до stop - 1, з кроком step

# Послідовність чисел
for i in range(5):
    print(i)

# З початком і кінцем
for i in range(2, 10):
    print(i)

# З кроком
for i in range(0, 10, 2):
    print(i)


# Функція Enumerate 
# - використовується для одночасного отримання індексу та значення елементів ітерованого об'єкта
some_list = ["apple", "banana", "cherry"]
for index, value in enumerate(some_list):
    print(index, value)


# Функція Zip
# - використовується для ітерації по декількох ітерованих об'єктах одночасно.
list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):
    print(number, letter)
# Вивід у консоль: зелене яблуко
# стигла вишня
# червоний томат

# Коли колекції, передані в zip, мають різну довжину, zip обробляє елементи до тих пір,
# поки не закінчаться елементи в найкоротшій колекції.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e'] #Елементи 'd' та 'e' будуть проігноровані

for number, letter in zip(list1, list2):
    print(number, letter)
# 1 a
# 2 b
# 3 c

#-------------
#Ітерування за словником
numbers = {
    1: "one",
    2: "two",
    3: "three"
}
for key in numbers:
    print(key)

# Перебирання за ключем словника. Можна перезаписувати значення
for key in numbers.keys():
    print(key)

# Перебирання за значенням словника
for val in numbers.values():
    print(val)

# Перебирання за парою ключ-значення
for key, value in numbers.items():
    print(key, value)

# !!!!Не можна видаляти та додавати елементи словника/списку під час ітерацій в циклі.


#-------------
# While
#Використовується коли кількість ітерацій заздалегідь невідома або коли ітерації 
#залежать від змінних, які можуть бути модифіковані в процесі виконання циклу.
k = 0
while k < 10:
    k = k + 1
    print(k)

#Break
a = 0
while True:
    print(a)
    if a >= 20:
        break
    a = a + 1

#Continue
a = 0
while a < 6:
    a = a + 1
    if not a % 2:
        continue
    print(a)

#Вкладені цикли

# while True:
#     number = input("number = ")
#     number = int(number)
#     while True:
#         print(number)
#         number = number - 1
#         if number < 0:
#             break


#Основні типи винятків
# SyntaxError — синтаксична помилка.
# IndentationError — помилка, яка виникає, якщо у виділенні блоків інструкцій пробілами допущена помилка.
# TabError виникає, якщо в одному файлі використовувати пробіли і табуляції для виділення блоків інструкцій.
# TypeError виникає, коли операція зі змінною цього типу неможлива. (2 / 'a')
# ValueError виникає, коли тип операнда відповідний, але значення таке, що операцію неможливо виконати. (int("a"))
# ZeroDivisionError — ділення на нуль.


# try ... except
val = 'a'
try:
    val = int(val)
except ValueError:
    print(f"val {val} is not a number")
else: # необов'язковий блок, який виконається тільки якщо винятків не сталося
    print(val > 0)
finally: # необов'язковий блок, який иконається у будь-якому разі, були помилки або ні.
    print("This will be printed anyway")

# Обробка через if-else (не шлях самурая)
age = input("How old are you? ")
try:
    age = int(age)
    if age >= 18:
        print("You are adult.")
    else:
        print("You are infant")
except ValueError:
    print(f"{age} is not a number") #f-рядок — це такий шаблон, який дозволяє 
    #зручним чином генерувати рядок, підставляючи результат виконання виразів у потрібне місце в шаблоні.



#-----------------------------Функції-----------------------------------
def say_hello():
		# тіло функції
    print('Привіт, Світ!')

# Кінець функції say_hello()

# виклик функції
say_hello()

# ще один виклик функції
say_hello()

# З параметрами
def print_max(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')

print_max(3, 4)  # пряма передача значень
x = 5
y = 7
print_max(x, y)  # передача змінних у якості аргументів


# Типізація параметрів
def print_max(a: int, b: int):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')

print_max(3, 4)  # пряма передача значень
x = 5
y = 7
print_max(x, y)  # передача змінних у якості аргументів

# Функція Return
# def my_function() -> ReturnType:
#     # виконати дії
#     return result

def add_numbers(num1: int, num2: int) -> int:
    sum = num1 + num2
    return sum

result = add_numbers(5, 10)
print(result)  # Виведе: 15

# String
def greet(name: str) -> str:
    return f"Привіт, {name}!"

greeting = greet("Олексій")
print(greeting)  # Виведе: Привіт, Олексій!

# Bool
def is_even(num: int) -> bool:
    return num % 2 == 0

check_even = is_even(4)
print(check_even)  # Виведе: True

# Незмінні типи:
#int, float, str, tuple

# Коли незмінний об'єкт передається у функцію, передається його копія, 
# зміни цього об'єкту в функції не впливають на оригінальний об'єкт.
def modify_list(lst: list) -> None:
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3, 4]

# Функція Copy
def modify_list(lst: list) -> None:
    lst = lst.copy()
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3]

# Задача: конвертувати кожен символ у рядку в його відповідний код ASCII.
def string_to_codes(string: str) -> dict:
    # Ініціалізація словника для зберігання кодів
    codes = {}  
    # Перебір кожного символу в рядку
    for ch in string:  
        # Перевірка, чи символ вже є в словнику
        if ch not in codes:
            # Додавання пари символ-код в словник  
            codes[ch] = ord(ch)  #функція приймає один символ і повертає його код ASCII
    return codes

result = string_to_codes("Hello world!")
print(result) # {'H': 72, 'e': 101, 'l': 108, 'o': 111, ' ': 32, 'w': 119, 'r': 114, 'd': 100, '!': 33}



#-----------------------------Області видимості (LEGB)-----------------------------------
# L - Local (Локальна): Це внутрішній рівень, де ім'я визначено всередині функції або блоку коду.

# E - Enclosing (Охоплювана): Це область видимості, яка охоплює локальну область видимості. 

# Якщо функція знаходиться всередині іншої функції, імена, визначені в охоплюваній функції, 
# будуть доступні для внутрішньої функції.

# G - Global (Глобальна): Це область видимості на рівні модуля або сценарію. 
# Змінні, визначені на цьому рівні, доступні у всьому модулі.

# B - Built-in (Вбудована): Це самий зовнішній рівень, який містить імена, вбудовані в Python. 
# Наприклад розглянуті нами вбудовані функції, len, range тощо.


# Local
x = 50

def func() -> None:
    x = 2
    print('Зміна локального x на', x)  # Зміна локального x на 2

func()
print('Глобальний x як і раніше', x)  # x як і раніше 50


# Enclosing 
def outer_func():
    enclosing_var = "Я змінна в функції, що охоплює"

    def inner_func(): # внутрішня функція може читати але не змінювати змінні
        print("Всередині вкладеної функції:", enclosing_var)

    inner_func()

outer_func()

# Зміна змінної в функції яку охоплює зовнішня функція
def func_outer():
    x = 2

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    return x

result = func_outer()  # 5


# Global
x = 50

def func():
    global x
    print('x дорівнює', x)  # x дорівнює 50
    x = 2
    print('Змінюємо глобальне значення x на', x)  # Змінюємо глобальне значення x на 2

func()
print('Значення x складає', x)# Значення x складає 2


#-----------------------------Ключові аргументи функції-----------------------------------
# Ключові аргументи в функціях Python — це спосіб передачі аргументів функції, при якому 
# кожному аргументу присвоюється ім'я. 

#Це дозволяє вказувати аргументи у будь-якому порядку під час виклику функції, 
# не дотримуючись порядку, визначеного у її оголошенні.

#Ex1
def greet(name, message="Привіт"):
    print(f"{message}, {name}!")

# використовує значення за замовчуванням для message
greet("Олексій")

# передача власного значення для message
greet("Марія", message="Добрий день")  

#Ex2
def func(a, b=5, c=10):
    print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)

# a дорівнює 3, b дорівнює 7, а c дорівнює 10
func(3, 7)

# a дорівнює 25, b дорівнює 5, а c дорівнює 24
func(25, c=24)

# a дорівнює 100, b дорівнює 5, а c дорівнює 50
func(c=50, a=100)


#-----------------------------Змінна кількість параметрів-----------------------------------
#Параметр *args. Він дозволяє функції приймати довільну кількість позиційних аргументів. 
# Аргументи, передані функції, зберігаються у вигляді кортежу.

#Параметр **kwargs. Він дозволяє функції приймати довільну кількість ключових аргументів. 
# Але аргументи, передані функції, зберігаються вже у вигляді словника.

# *args

#Ex1
def print_all_args(*args):
    for arg in args:
        print(arg)

print_all_args(1, 'hello', True)

#Ex2
def concatenate(*args) -> str:
    result = ""
    for arg in args:
        result += arg
    return result

print(concatenate("Hello", " ", "world", "!"))


# **kwargs
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", age=25) #name: Alice age: 25

# !!!!Коли ви використовуєте обидва ці параметри разом, *args має йти перед **kwargs. 
# Тоді параметр *args збере всі позиційні аргументи в кортеж, а **kwargs збере всі 
# ключові аргументи в словник.
def example_function(*args, **kwargs):
    print("Позиційні аргументи:", args)
    print("Ключові аргументи:", kwargs)

example_function(1, 2, 3, name="Alice", age=25)


#-----------------------------Розпакування списків та словників-----------------------------------
# дозволяє присвоїти значення зі списку або словника до змінних одним рядком коду
my_list = [1, 2, 3]
a, b, c = my_list

a, _, c = my_list # ігнорування деяких елементів списку

a, *rest = my_list # розпаковка частини списку; 
#rest стане списком, що містить всі інші елементи та дорівнюватиме [2, 3]

# Розпакування словника
# використовується під час передачі аргументів у функцію
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

person_info = {"name": "Alice", "age": 25}
greet(**person_info)


#-----------------------------Рекурсія-----------------------------------
# Основні компоненти рекурсії:
# Базовий випадок: Це умова, при якій рекурсія припиняє виклик самої себе, 
# щоб уникнути нескінченного циклу. Він важливий для запобігання нескінченному циклу в рекурсії.

# Рекурсивний випадок: Це умова, за якої функція викликає саму себе з новими аргументами. 
# Фактично це ситуація, коли функція продовжує викликати саму себе, розбиваючи проблему на менші частини.

# обчислення факторіала
def factorial(n):
    if n == 0: # базовий випадок
        return 1
    else:
        return n * factorial(n-1) # рекурсивний випадок

print(factorial(5)) # виведе 120

# Числа Фібоначчі
def fibonacci(n):
    if n <= 1: # базовий випадок
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) # рекурсивний випадок

print(fibonacci(10)) # виведе 55

