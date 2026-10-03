def add_tasks(tasks, task):
    try:
        if not isinstance(tasks, list):
            raise TypeError("Ожидался список задач, а не " + type(tasks).__name__)

        if not isinstance(task, str) or not task.strip():
            raise ValueError("Задача должна быть непустой строкой")

        tasks.append(task)
        print(f"Задача '{task}' была добавлена!")

    except TypeError as e:
        print(f"Ошибка типа: {e}")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except Exception as e:
        print(f"Непредвиденная ошибка при добавлении: {e}")


def list_task(tasks):
    try:
        if not isinstance(tasks, list):
            raise TypeError("Ожидался список задач, а не " + type(tasks).__name__)

        if len(tasks) == 0:
            print("Список задач пуст.")
            return

        print("Список задач:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

    except TypeError as e:
        print(f"Ошибка типа: {e}")
    except Exception as e:
        print(f"Непредвиденная ошибка при выводе: {e}")


def delete_list(tasks):
    try:
        if not isinstance(tasks, list):
            raise TypeError("Ожидался список задач, а не " + type(tasks).__name__)

        if not tasks:
            print("Список задач пуст — нечего удалять.")
            return

        print("Список задач:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

        try:
            number = int(input("Введите номер задачи для удаления: "))
            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(f"Задача '{removed}' была удалена!")
            else:
                print("Нет задачи с таким номером.")
        except ValueError:
            print("Нужно ввести число.")

    except TypeError as e:
        print(f"Ошибка типа: {e}")
    except Exception as e: