def task_1_variant_1():
    B = [3, 2, -5, 4, -1, 8, -10, 5]
    print(f"Початковий список B: {B}")

    negatives = [x for x in B if x < 0]

    if not negatives:
        print("У списку немає від'ємних елементів.")
        return

    max_negative = max(negatives)
    print(f"Найбільший від'ємний елемент: {max_negative}")

    max_neg_index = B.index(max_negative)
    new_B = []

    for i in range(len(B)):
        if i < max_neg_index:
            new_B.append(B[i] ** 2)
        else:
            new_B.append(B[i])

    print(f"Результат (новий список): {new_B}")

if __name__ == "__main__":
    task_1_variant_1()