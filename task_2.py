print("Вводьте числа:")

prev = int(input())
count = 0

if prev != 0:
    while True:
        curr = int(input())
        if curr == 0:
            break
        if curr > prev:
            count += 1
        prev = curr

print("Кількість елементів, більших за попередній:", count)
