import datetime

input_time_in_s = input("Input time in seconds:")
input_time_in_s = int(input_time_in_s)
print(
    'You entered: %d:%d:%d' % (input_time_in_s // 3600, (input_time_in_s % 3600) // 60, (input_time_in_s % 3600) % 60))

# Вариант вывода в формате hh:mm:ss с использованием библиотеки datetime
print('You entered:',
      datetime.time(input_time_in_s // 3600, (input_time_in_s % 3600) // 60, (input_time_in_s % 3600) % 60))

# Без использования библиотеки datetime
if (input_time_in_s // 3600) < 10:
    input_time_hours = "0" + str(input_time_in_s // 3600)
if ((input_time_in_s % 3600) // 60) < 10:
    input_time_minutes = "0" + str((input_time_in_s % 3600) // 60)
if ((input_time_in_s % 3600) % 60) < 10:
    input_time_seconds = "0" + str((input_time_in_s % 3600) % 60)
print('You entered: %s:%s:%s' % (input_time_hours, input_time_minutes, input_time_seconds))

