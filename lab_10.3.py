import matplotlib.pyplot as plt


def task_3_simple():
    with open("text.txt", "r", encoding="utf-8") as f:
        text = f.read().lower()

    vowels_list = list("аеєиіїоуюя")
    counts = []

    for letter in vowels_list:
        n = text.count(letter)
        counts.append(n)

    plt.bar(vowels_list, counts)

    plt.savefig("my_histogram.png")
    plt.show()

if __name__ == "__main__":
    task_3_simple()