import datetime

input_time_in_s = int(input("Input time in seconds:"))

# Вариант вывода в формате hh:mm:ss с использованием библиотеки datetime, в случае такого решения есть ограничение на
# количетсво часов, их должно быть <= 24
print('You entered:',
      datetime.time(input_time_in_s // 3600, (input_time_in_s % 3600) // 60, (input_time_in_s % 3600) % 60))

# Без использования библиотеки datetime
if (input_time_in_s // 3600) < 10:
    input_time_hours = "0" + str(input_time_in_s // 3600)
else:
    input_time_hours = str(input_time_in_s // 3600)

if ((input_time_in_s % 3600) // 60) < 10:
    input_time_minutes = "0" + str((input_time_in_s % 3600) // 60)
else:
    input_time_minutes = str((input_time_in_s % 3600) // 60)

if ((input_time_in_s % 3600) % 60) < 10:
    input_time_seconds = "0" + str((input_time_in_s % 3600) % 60)
else:
    input_time_seconds = str((input_time_in_s % 3600) % 60)

print('You entered: %s:%s:%s' % (input_time_hours, input_time_minutes, input_time_seconds))
