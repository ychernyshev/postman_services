import time

time_count = 5

for i in range(time_count, 0, -1):
    print('Осталось %d секунд' % i)
    time.sleep(1)
print('Пуск!!!')