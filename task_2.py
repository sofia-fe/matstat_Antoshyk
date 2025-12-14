print("Введіть п'ятизначне число:")
number = input()

sum1 = int(number[0]) + int(number[2]) + int(number[4])
sum2 = int(number[1]) + int(number[3])

print(sum1, sum2, sep="")