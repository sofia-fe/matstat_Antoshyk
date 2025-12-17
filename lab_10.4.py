import numpy as np


def task_4():
    arr1 = np.array([10, 20, 30, 40, 50])
    arr2 = np.array([2, 4, 5, 8, 10])

    print(f"Масив 1: {arr1}")
    print(f"Масив 2: {arr2}")
    print("-" * 30)

    print("АРИФМЕТИЧНІ ОПЕРАЦІЇ:")

    add_result = arr1 + arr2
    print(f"Сума (arr1 + arr2):      {add_result}")

    sub_result = arr1 - arr2
    print(f"Різниця (arr1 - arr2):   {sub_result}")

    mul_result = arr1 * arr2
    print(f"Добуток (arr1 * arr2):   {mul_result}")

    div_result = arr1 / arr2
    print(f"Частка (arr1 / arr2):    {div_result}")

    print("-" * 30)

    combined_array = np.concatenate([arr1, arr2])
    print(f"Об'єднаний масив: {combined_array}")
    print("-" * 30)

    max_val = combined_array.max()
    print(f"Максимальний елемент: {max_val}")

    min_val = combined_array.min()
    print(f"Мінімальний елемент:  {min_val}")

    sum_val = combined_array.sum()
    print(f"Сума всіх елементів:  {sum_val}")

    prod_val = combined_array.prod()
    print(f"Добуток всіх елементів: {prod_val}")


if __name__ == "__main__":
    task_4()