def task_2():
    filename = "task_2_output.txt"

    with open(filename, "w") as file:
        for i in range(1, 10):
            line = "a" * i
            file.write(line + "\n")

    print(f"Файл '{filename}' успішно створено!")

if __name__ == "__main__":
    task_2()