print("Введіть кількість учнів у першому класі:")
a = int(input())

print("Введіть кількість учнів у другому класі:")
b = int(input())

print("Введіть кількість учнів у третьому класі:")
c = int(input())

desks_a = (a + 1) // 2
desks_b = (b + 1) // 2
desks_c = (c + 1) // 2

total = desks_a + desks_b + desks_c

print("Всього потрібно парт:", total)