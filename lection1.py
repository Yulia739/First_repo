print("Hello World")

#об'єднаний рядок
s1 = "Hello"
s2 = "world!"
joined_string = s1 + " " + s2
#або joined_string = f"{s1} {s2}"

#f-рядок — це такий шаблон, який дозволяє зручним чином генерувати рядок, підставляючи результат виконання виразів у 
# потрібне місце в шаблоні.
name = "Oleg"
hello_string = f"Hello, {name}!"

#Приклад None - змінна або вираз не мають конкретного значення
connect_to_database = None

#Приклад інструкцій (statement)
#Інструкції виконуються почергово зліва направо та зверху вниз
x = 2
y = x + 10
x = 100; print("Hello world!")

#Вираз (expression)
a = 1
b = 2
c = a + b + 10

#Оператори
#Приклад обчислення кількості годин, хвилин і секунд у заданій кількості секунд n.
n = 5000

hours = n // (60 * 60) #// - операція ділення без остачі
minutes = (n - hours * 60 * 60) // 60
seconds = n - hours * 60 * 60 - minutes * 60

#Залишок від ділення
10 % 3 #поверне 1, оскільки 10 ділиться на 3 три рази із залишком 1.
#Перевірка на парність
x % 2 #дорівнює 0, тоді x є парним/якщо вираз дорівнює 1, тоді x є непарним.

#Зведення негативного числа у ступінь. Пріоритет операції зведення в степінь вищий за заперечення, тому беремо в дужки.
(-3) ** 2  # 9
#Пріорітети операцій:
#- ()
#- **
#- Унарні +, -
#- *, /, //
#- +, -
#- ==, !=, >, <, >=, <=
#- not, and, or

#Функція виводу данних
print("Hello world!")

#Функція введення данних
#введення з input() завжди є рядком
a = input("Рядок запрошення: ")


#Приведення типів
age = input("How old are you? ")
age = int(age)

pi = float('3.14') #з рядка у float

pi_str = str(3.14)
age_str = str(29)

#Зазвичай числове значення 0, порожні колекції ([], (), {}) та None перетворюються на False. Усе інше — на True.
bool(0)  # False
bool(1)  # True

#Символ \ використовується в кінці рядка для вказівки на те, що вираз продовжується на наступному рядку.
#Після \ не повинно бути жодних інших символів, навіть пробілів або коментарів, до кінця рядка
#total_cost = num_croissants * price_per_croissant + \
#             num_glasses * price_per_glass + \
#             num_coffee_packs * price_per_coffee_pack

#Оператор / ділення завжди повертає результат ділення як дійсне число float, навіть якщо обидва операнди є цілими числами.
#Оператор // цілочисельного ділення повертає результат ділення з відкиданням дробової частини. Може повертати int або float 
#(якщо один з операндів був float)



#Основні типи колекцій
# -Списки (Lists). Змінні
# -Кортежі (Tuples). Незмінні
# -Словники (Dictionaries). Пара ключ-значення. Значенням може бути будь-який тип даних.
# -Множини (Sets). Неупорядковані колекції. Використовуються для операцій об'єднання, перетин, різниця
# -Заморожені множини (Frozen Sets). Незмінні


#----------------------------------------------------------------------------------------------
#Список

#Створення порожнього списку
my_list = list()
empty_list = []
my_list = [1, "Hello", 3.14]

#Додавання числа в кінець списку
my_list.append(4)

#Видалення елементу
my_list.remove("Hello")

#Доступ за індексом
some_iterable = ["a", "b", "c"]
first_letter = some_iterable[0]
middle_one = some_iterable[1]
last_letter = some_iterable[2]

#Індексування елементів з кінця
some_iterable = ["a", "b", "c"]
first_letter = some_iterable[-3]
middle_one = some_iterable[-2]
last_letter = some_iterable[-1]

#Зміна елемента за індексом
some_iterable[1] = -2

#Знаходження та видалення елемента за індексом (елемент b)
last = some_iterable.pop(1)

#Розширення списку
chars = ['a', 'b', 'c']
numbers = [1, 2]
chars.extend(numbers)

#Додавання елемента в середину списку
chars = ["a", "c"]
chars.insert(1, "b") #отримаємо список ['a', 'b', 'c']

#Повністю очищує список
chars = ['a', 'b']
chars.clear() # []

#Знаходження індексу першого входження заданого елемента у списку
chars = ['a', 'b', 'c', 'd']
c_ind = chars.index('c') #c_ind = 2

#Підрахунок кількості разів, скільки певний елемент зустрічається у списку
my_list = [1, 2, 3, 4, 2, 2, 5, 2]
count_2 = my_list.count(2)
print(count_2)  # Виведе 4, оскільки число 2 зустрічається 4 рази

#Підраховує кількість елементів
my_list = [1, 2, 3, 4, 5]
print(len(my_list))

#Сортування у порядку зростання (за замовчуванням)
nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort()
print(nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]

#Спадання
nums.sort(reverse=True)
print(nums)  # Виведе [9, 5, 4, 3, 2, 1, 1]

#Сортування за ключем (наприклад довжина слова)
words = ["banana", "apple", "cherry"]
words.sort(key=len)
print(words)  # Виведе ['apple', 'banana', 'cherry']

#Функція sorted() повертає новий відсортований соб'єкт, залишаючи вихідний об'єкт без змін.
#Сортування у порядку зростання (за замовчуванням)
nums = [3, 1, 4, 1, 5, 9, 2]
sorted_nums = sorted(nums)
print(sorted_nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]

#Спадання
sorted_nums_desc = sorted(nums, reverse=True)
print(sorted_nums_desc)  # Виведе [9, 5, 4, 3, 2, 1, 1]

#Повертає копію списку
chars =  ['a', 'b']
chars_copy = chars.copy()
#Створено змінну chars_copy, де зберегли копію списку chars

#Зміна порядку елементів на зворотній
chars = ["banana", "apple", "cherry"]
chars.reverse()




#------------------------------------------------------------------------------------------
#Словник

#Створення порожнього словника
my_dict = {}

my_dict = {"name": "Alice", "age": 25, "city": "New York"}

#Доступ за ключем
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict["name"])  # Виведе 'Alice'

#Зміна або додавання нової пари ключ-значення
my_dict["age"] = 26  # Змінює вік на 26
my_dict["email"] = "alice@example.com"  # Додає нову пару ключ-значення
print(my_dict)

#Видалення за ключем
del my_dict["age"]
print(my_dict)

#Перевірка чи є ключ у словнику
print("name" in my_dict) #True
print("age" in my_dict) #False

#Видаляє елемент та повертає його значення
my_dict = {"name": "Alice", "age": 25}
age = my_dict.pop("age") #змінна age отримає значення 25, а пара ключ-значення "age": 25 буде видалена зі словника

#Оновлення словника іншим словником або парами ключ-значення
my_dict = {"name": "Alice", "age": 25}
my_dict.update({"email": "alice@example.com", "age": 26}) #словник my_dict буде оновлено новими парами 
#ключ-значення, де ключ "email" буде додано в словник, а значення ключа "age" буде оновлено.

#Повністю очищає словник
my_dict.clear()

#Створення поверхневої копії словника
new_dict = my_dict.copy() #new_dict буде новим словником з тими самими парами ключ-значення, що і my_dict, але як окремий об'єкт

#Безпечне отримання значення за ключем зі словника. Не викликає помилку, якщо ключ не знайдено
my_dict = {"name": "Alice", "age": 25}
age = my_dict.get("age")  # Поверне 25
gender = my_dict.get("gender")  # Поверне None, оскільки "gender" немає в словнику

#При використанні [] поверне помилку, якщо не булшо знайдено
name = my_dict["name"]  # Поверне 'Alice'
gender = my_dict["gender"]  # Викличе KeyError, оскільки "gender" немає в словнику
#Краще використовувати get



#------------------------------------------------------------------------------------------
#Множина

#Створення порожньої множини
empty_set = set()

a = set('hello')
b = {1, 2, 3, 4, 5}
numbers = {1, 2, 3, 1, 2, 3}
#Не мають визначеного порядку елементів (не можна звернутись через індекс)

#Видалення дублікатів зі списку
lst = [1, 2, 3, 1, 2, 2, 3, 4, 1]
d_lst = set(lst) #перетворюємо список у множину
lst=list(d_lst) #перетворюємо множину у список

#Додавання елемента
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)  # {1, 2, 3, 4}

#Видалення елемента (викликає виняток, якщо такого елемента немає)
numbers = {1, 2, 3}
numbers.remove(3)
print(numbers)  # {1, 2}

#Видалення елемента (не викликає вийняток, якщо його немає у списку)
numbers = {1, 2, 3}
numbers.discard(2)
print(numbers)  # {1, 3}

#Математичні операції

#Загальні елементи для двох множин (спільні елементи)
a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))  # {3}
print(a & b)  # {3}

#Різниця між множинами
a = {1, 2, 3}
b = {3, 4, 5}
print(a.difference(b))  # {1, 2}
print(a - b)  # {1, 2}

#Пошук всіх елементів з двох множин, окрім загальних
a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}
print(a ^ b)  # {1, 2, 4, 5}

#Об'єднання двох множин
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}
print(a | b)  # {1, 2, 3, 4, 5}

#Створення замороженної множини (її дані не можуть додаватись або видалятись)
my_frozenset = frozenset([1, 2, 3, 4, 5])

#Можна використовувати такі операції як: об'єднання, перетин і різниця
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

union = a | b  # Об'єднання множин
intersection = a & b  # Перетин множин
difference = a - b  # Різниця множин
symmetric_difference = a ^ b  # Симетрична різниця

print(union)  # frozenset({1, 2, 3, 4, 5})
print(intersection)  # frozenset({3})
print(difference)  # frozenset({1, 2})
print(symmetric_difference)  # frozenset({1, 2, 4, 5})




#------------------------------------------------------------------------------------------
#Кортеж. Незмінний

#Створення порожнього кортежа
my_tuple = tuple() # або
my_tuple = ()

my_tuple = (1, 2, 3)
my_tuple = (1, "Hello", 3.14)
my_tuple = 1, "Hello", 3.14 #Упакування кортежу (створення без дужок)


#Кортеж з одним елементом
my_tuple = (1,)

#Доступ до елементів за індексом
first_item = my_tuple[0]  # Отримати перший елемент

#Кортежі можуть використовуватись в якості ключів для словників.
points = {
    (0, 0): "O",
    (1, 1): "A",
    (2, 2): "B"
} #У словнику points використовуються кортежі з координатами точок як ключі, а значення — це імена (назва) точок.





#------------------------------------------------------------------------------------------
#Рядки. 
#Рядки в Python є незмінними (immutable), це значить, що ви не можете змінити окремі символи в рядку без створення нового рядка.

game_string = 'My favorite "Game"'

#Звернення за індексом
s = "Hello world!"
print(s[0])# H
print(s[-1])# !


s = "Hello world!"
s[0] = "Q"# Тут буде викликано виняток (помилка) TypeError


#Переведення усіх літер у верхній регістр
s = "Hello" 
print(s.upper()) # Виведе 'HELLO'

#Переведення усіх літер у нижній регістр
s = "Some Text"
print(s.lower())  # Виведе 'some text'

#Перевірка, що рядок починається з підрядка
s = "Bill Jons"
print(s.startswith("Bi"))  # Виведе True

#Перевірка, що рядок закінчіється підрядком
s = "hello.jpg"
print(s.endswith("jpg"))  # Виведе True

#Перетворює перший символ рядка з великої літери, а інші з маленької
s = "hello world".capitalize()  # Результат: "Hello world"


#Перетворює перші літери кожного слова в рядку на великі
s = "hello world".title()  # Результат: "Hello World"

#Перевірка чи складається рядок тільки з цифр, літер, побілів
"123".isdigit()  # True
"hello".isalpha()  # True
" ".isspace()  # True


#Форматування рядків (format)
# Просте форматування рядка
name = 'John'
print('Hello, {}!'.format(name))

# Форматування з декількома аргументами
age = 25
print('Hello, {}. You are {} years old.'.format(name, age))

# Використання іменованих аргументів
print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# Використання індексів для вказівки порядку аргументів
print('Hello, {1}. You are {0} years old.'.format(age, name))



#------------------------------------------------------------------------------------------
#Зрізи (Slice). послідовність[початок:кінець:крок]

#Отримання перших 5 літер (кома не була включена по індексу 5)
s = "Hello, World!"
first_five = s[:5]
print(first_five)  # Виведе 'Hello'


#Отримуємо непарні числа
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = numbers[0:10:2]
#За замовчуванням зріз іде від початку до кінця, тому можна записати як:
odd_numbers = numbers[::2]  # Виведе [1, 3, 5, 7, 9]

#Отримуємо парні числа
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = numbers[1:10:2]
#або
even_numbers = numbers[1::2] # Виведе [2, 4, 6, 8, 10]

#Отримуємо числа кратні 3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
three_numbers = numbers[2:10:3]
#або
three_numbers = numbers[2::3]


#Від'ємні індекси для проходження списку з зворотньому напрямку
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_numbers = numbers[::-1]
print(reverse_numbers) #Змінна reverse_numbers буде зберігати зворотний список [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


#Копія списку
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
copy_numbers = numbers[:] #Зріз [:] вказує на вибір усіх елементів зі списку, починаючи з першого і закінчуючи останнім
print(copy_numbers)
