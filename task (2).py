import task

tasks = []

while True:
    try:
        command = input("Введите команду (add/list/delete/exit): ").strip().lower()
    except (KeyboardInterrupt, EOFError):
        print("\nЗавершение работы.")
        break

    if command == "exit":
        print("До свидания!")
        break
    elif command == "add":
        message = input("Введите задачу: ")
        task.add_tasks(tasks, message)
    elif command == "list":
        task.list_task(tasks)
    elif command == "delete":
        task.delete_list(tasks)
    elif command == "":
        continue
    else:
        print("Неизвестная команда. Доступные: add, list, delete, exit")

input("\nНажмите Enter для выхода...")