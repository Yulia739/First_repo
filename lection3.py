#-----------------------------Модулі datetime та time-----------------------------------
# Основні можливості datetime:

# визначення поточної дати і часу;
# обчислення інтервалу між двома подіями;
# визначення дня тижня, високосного року для будь-якої дати у минулому не раніше року datetime.MINYEAR або в майбутньому не пізніше року datetime.MAXYEAR;
# порівняння дати і часу декількох подій за допомогою операторів порівняння;
# робота з часовими зонами, порівняння подій з урахуванням часових зон та переходу на літній/зимовий час;
# перетворення дати/часу в рядок і навпаки.

#---------datetime---------
# Ex1
import datetime
# Або 
from datetime import datetime
now = datetime.datetime.now() # поточна дата та час
print(now) #2023-12-14 12:39:29.992996

# Ex2
from datetime import datetime

current_datetime = datetime.now()

print(current_datetime.year) # year: Повертає рік дати. 
#Наприклад, якщо now містить дату "2023-12-14 12:39:29", now.year буде 2023.

print(current_datetime.month) # month: Повертає місяць як число від 1 до 12. 
#У нашому прикладі now.month буде 12.

print(current_datetime.day) # day: Повертає день місяця. Для "2023-12-14 12:39:29" now.day буде 14.

print(current_datetime.hour) # hour: Повертає годину дня від 0 до 23. У нашому випадку now.hour буде 12.

print(current_datetime.minute) # minute: Повертає хвилини часу від 0 до 59. 
#Для даної дати now.minute буде 39.

print(current_datetime.second) # second: Повертає секунди часу від 0 до 59. 
#В нашому прикладі now.second буде 29.

print(current_datetime.microsecond) ## microsecond: Повертає мікросекунди часу. 
#Це значення може бути від 0 до 999999. У "2023-12-14 12:39:29.992996", now.microsecond буде 992996.

print(current_datetime.tzinfo) ## tzinfo: Повертає інформацію про часову зону об'єкта datetime. 
#Для now, якщо часова зона не була вказана, tzinfo буде None.

# Отримати дату (без часу) та час (без дати)
from datetime import datetime

current_datetime = datetime.now()
print(current_datetime.date()) #2023-12-14
print(current_datetime.time()) #12:59:06.709007


# Зворотний метод datetime.combine
# створює новий об'єкт datetime шляхом комбінування об'єктів date та time
# Ex1
import datetime

# Створення об'єктів date і time
date_part = datetime.date(2023, 12, 14)
time_part = datetime.time(12, 30, 15)

# Комбінування дати і часу в один об'єкт datetime
combined_datetime = datetime.datetime.combine(date_part, time_part)

print(combined_datetime)  # Виведе "2023-12-14 12:30:15"

# Ex2
# Створення об'єкта datetime з конкретною датою
import datetime
specific_date = datetime.datetime(year=2020, month=1, day=7)

print(specific_date)  # Виведе "2020-01-07 00:00:00"

# Ex3
# Створення об'єкта datetime з конкретною датою і часом
import datetime
specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)

print(specific_datetime)  # Виведе "2020-01-07 14:30:15"

#АБО

import datetime
# Створення об'єкта datetime з конкретною датою і часом
specific_datetime = datetime.datetime(2020, 1, 7, 14, 30, 15)

print(specific_datetime)  # Виведе "2020-01-07 14:30:15"


#---------Метод weekday()---------
# використовується для отримання номера дня тижня для вказаної дати (понеділок має номер 0, а неділя - 6).

from datetime import datetime

# Створення об'єкта datetime
now = datetime.now()

# Отримання номера дня тижня
day_of_week = now.weekday()

# Поверне число від 0 (понеділок) до 6 (неділя)
print(f"Сьогодні: {day_of_week}")  

#---------Порівняння datetime---------
from datetime import datetime

# Створення двох об'єктів datetime
datetime1 = datetime(2023, 3, 14, 12, 0)
datetime2 = datetime(2023, 3, 15, 12, 0)

# Порівняння дат
print(datetime1 == datetime2)  # False, тому що дати не однакові
print(datetime1 != datetime2)  # True, тому що дати різні
print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2


#-----------------------------Робота з часовими проміжками timedelta--------------------
# Об'єкти timedelta можуть представляти дні, години, хвилини, секунди та мікросекунди.
# Вони корисні для розрахунків, що включають додавання або віднімання часу від конкретних дат 
# або порівняння часових інтервалів.
# Максимальний діапазон для timedelta обмежений приблизно 9999 роками.
from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta) #64 days, 8:05:56.000010
#Якщо якийсь параметр не заданий, то він дорівнює 0 за замовчуванням.


# Відмімання одного datetime від іншого дасть timedelta об'єкт.
# Він відповідає за відрізок часу між двома датами.
from datetime import datetime

seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

difference = seventh_day_2020 - seventh_day_2019
print(difference)  # 365 days, 0:00:00
#конвертація timedelta в секунди
print(difference.total_seconds())  # 31536000.0

# Додавання до дати
from datetime import datetime, timedelta

now = datetime.now()
future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
print(future_date) #2023-12-28 14:08:46.342976

# Від конкретної дати
from datetime import datetime, timedelta

seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
four_weeks_interval = timedelta(weeks=4)

print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00


#---------Метод toordinal()---------
# повертає порядковий номер дня, враховуючи кількість днів з 1 січня року 1 нашої ери
# Цей метод перетворює об'єкт datetime в ціле число, що представляє порядковий номер даного дня.

# Ex1
from datetime import datetime

# Створення об'єкта datetime
date = datetime(year=2023, month=12, day=18)

# Отримання порядкового номера
ordinal_number = date.toordinal()
print(f"Порядковий номер дати {date} становить {ordinal_number}") 
#Виведе: Порядковий номер дати 2023-12-18 00:00:00 становить 738872


# Ex2
from datetime import datetime

# Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# Поточна дата
current_date = datetime.now()

# Розрахунок кількості днів
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
print(days_since) # 77161


#-----------------------------Робота timestamp--------------------
# використовується для вказівки конкретного моменту в часі (кількість секунд).

# Конвертація datetime в timestamp
from datetime import datetime

# Поточний час
now = datetime.now()

timestamp = datetime.timestamp(now)
print(timestamp)  # Виведе timestamp поточного часу
# Виведе: 1702854066.56633


# Конвертація timestamp назад у datetime
from datetime import datetime

# Припустимо, є timestamp
timestamp = 1617183600

dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)  # Виведе відповідний datetime
# Виведе: 2021-03-31 12:40:00



#---------Парсинг дати із рядка---------

#---------Метод strftime---------
# використовується для форматування об'єктів дати та часу datetime у рядки 
# за допомогою специфічних форматних кодів.

# Кожен код у рядку формату починається з символу % і представляє певний компонент дати або часу. 
# Ось деякі з найбільш використовуваних кодів:

# %Y - рік з чотирма цифрами (наприклад, 2023).
# %y - рік з двома цифрами (наприклад, 23).
# %m - місяць як номер (наприклад, 03 для березня).
# %d - день місяця як номер (наприклад, 14).
# %H - година (24-годинний формат) (наприклад, 15).
# %I - година (12-годинний формат) (наприклад, 03).
# %M - хвилини (наприклад, 05).
# %S - секунди (наприклад, 09).
# %A - повна назва дня тижня (наприклад, Tuesday).
# %a - скорочена назва дня тижня (наприклад, Tue).
# %B - повна назва місяця (наприклад, March).
# %b або %h - скорочена назва місяця (наприклад, Mar).
# %p - AM або PM для 12-годинного формату.

# Ex1
from datetime import datetime

now = datetime.now()

# Форматування дати і часу
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date) 

# Форматування лише дати
formatted_date_only = now.strftime("%A, %d %B %Y")
print(formatted_date_only)

# Форматування лише часу
formatted_time_only = now.strftime("%I:%M %p")
print(formatted_time_only)  

# Форматування лише дати
formatted_date_only = now.strftime("%d.%m.%Y")
print(formatted_date_only)
# Виведення:
# 2023-12-18 01:37:07
# Monday, 18 December 2023
# 01:37 AM
# 18.12.2023

#---------Метод strptime---------
# Цей метод є протилежністю до strftime, який перетворює об'єкти datetime у рядки
# Коди форматування для strptime такі ж, як і для strftime. 
# Наприклад, %Y представляє рік із чотирма цифрами, %m - місяць у вигляді двоцифрового числа тощо.

from datetime import datetime

# Припустимо, у нас є дата у вигляді рядка
date_string = "2023.03.14"

# Перетворення рядка в об'єкт datetime
datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу
#Виведення: 2023-03-14 00:00:00

import pytz #timezone


# ISO формат дати ("YYYY-MM-DDTHH:MM:SS")

from datetime import datetime
# Поточна дата та час
now = datetime.now()

# Ex1
# Конвертація у формат ISO 8601
iso_format = now.isoformat()
print(iso_format)
from datetime import datetime
iso_date_string = "2023-03-14T12:39:29.992996"

# Ex2
# Конвертація з ISO формату
date_from_iso = datetime.fromisoformat(iso_date_string)
print(date_from_iso)


# Ex3
from datetime import datetime

# Створення об'єкта datetime
now = datetime.now()

# Використання isoweekday() для отримання дня тижня
day_of_week = now.isoweekday()

print(f"Сьогодні: {day_of_week}")  # Поверне число від 1 до 7, що відповідає дню тижня

#----------isocalendar----------
from datetime import datetime

# Створення об'єкта datetime
now = datetime.now()

# Отримання ISO календаря
iso_calendar = now.isocalendar()

print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")

# Метод isoformat() використовується для конвертації об'єкта datetime в рядок у форматі ISO 8601.
# Метод fromisoformat() використовується для конвертації рядка у форматі ISO 8601 в об'єкт datetime.
# Метод isoweekday() використовується для отримання дня тижня відповідно до ISO 8601.
# Метод isocalendar() використовується для отримання кортежу, що містить ISO рік, 
# номер тижня в році та номер дня тижня відповідно до ISO 8601.


#---------------Таймзони---------------
from datetime import datetime, timezone, timedelta

# Припустимо, місцевий час належить до часової зони UTC+2
local_timezone = timezone(timedelta(hours=2))
local_time = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)

# Конвертація локального часу в UTC
utc_time = local_time.astimezone(timezone.utc)
print(utc_time)  # Виведе час в UTC


# Ex2
from datetime import datetime, timezone, timedelta

# Час у конкретній часовій зоні
timezone_offset = timezone(timedelta(hours=2))  # Наприклад, UTC+2
timezone_datetime = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)

# Конвертація у формат ISO 8601
iso_format_with_timezone = timezone_datetime.isoformat()
print(iso_format_with_timezone)



#------Робота з часом--------

import time

current_time = time.time() #повертає поточний час у секундах з 1 січня 1970 року
print(f"Поточний час: {current_time}")

# Метод time.sleep(seconds)
import time

print("Початок паузи")
time.sleep(5) #зупиняє виконання програми на 5 секунд.
print("Кінець паузи")


# Метод time.ctime([seconds])
#перетворює часову мітку (кількість секунд) у зрозуміле для людини текстове представлення
import time

current_time = time.time()
print(f"Поточний час: {current_time}")

readable_time = time.ctime(current_time)
print(f"Читабельний час: {readable_time}")

# Метод time.localtime([seconds])
#перетворює часову мітку в структуру struct_time у місцевій часовій зоні.
import time

current_time = time.time()
print(f"Поточний час: {current_time}")

local_time = time.localtime(current_time)
print(f"Місцевий час: {local_time}")
# Виведення:
# Поточний час: 1702861070.8583968
# Місцевий час: time.struct_time(tm_year=2023, tm_mon=12, tm_mday=18, tm_hour=2, tm_min=57, 
# tm_sec=50, tm_wday=0, tm_yday=352, tm_isdst=0)

# метод time.perf_counter()
#надає доступ до лічильника з високою точністю, та є ідеальним для вимірювання коротких інтервалів часу.
#повертає значення в секундах (як дійсне число) з деякого моменту, наприклад з моменту запуску програми, 
# і це значення монотонно збільшується.

import time
# Записуємо час на початку виконання
start_time = time.perf_counter()

# Виконуємо якусь операцію
for _ in range(1_000_000): #"_" - зробити великі числа більш читабельними (=1000000)
    pass  # Просто проходить цикл мільйон разів

# Записуємо час після виконання операції
end_time = time.perf_counter()

# Розраховуємо та виводимо час виконання
execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд") #Час виконання: 0.04927480001060758 секунд

# time.time(): Повертає поточний час у секундах з 1 січня 1970 року (epoch time).
# time.sleep(seconds): Зупиняє виконання програми на вказану кількість секунд.
# time.ctime([seconds]): Перетворює часову мітку в текстове представлення, зрозуміле для людини.
# time.localtime([seconds]): Перетворює часову мітку в структуру struct_time у місцевій часовій зоні.
# time.gmtime([seconds]): Аналогічно localtime, але повертає struct_time у форматі UTC.
# time.perf_counter(): Повертає лічильник з високою точністю для вимірювання коротких інтервалів часу.



