x = 0
y = 0

print("Вводьте дані (наприклад 'Північ 5'), щоб завершити введіть 'Скарб!'):")

while True:
    line = input()
    if line == "Скарб!" or line == "Treasure!":
        break

    parts = line.split()

    direction = parts[0]
    steps = int(parts[1])

    if direction == "Північ" or direction == "North":
        y += steps
    elif direction == "Південь" or direction == "South":
        y -= steps
    elif direction == "Схід" or direction == "East":
        x += steps
    elif direction == "Захід" or direction == "West":
        x -= steps

print(x, y)