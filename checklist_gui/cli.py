from checklist_gui import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add, show, display, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        # Strip the return at the end of each todo done line 28
        # new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1} - {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number - 1] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            print(f"The todo '{todo_to_remove}' has been removed from the list")
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("You entered an unknown command")

print("Bye!")

###
# match user_action:
#         case 'add':
#             todo = input("Enter a todo: ") + "\n"
#
#             with open("todos.txt", "r") as file:
#                 todos = file.readlines()
#
#             todos.append(todo)
#
#             with open("todos.txt", "w") as file:
#                 file.writelines(todos)
#
#         case "show" | "display":
#             with open("todos.txt", "r") as file:
#                 todos = file.readlines()
#
#             # Strip the return at the end of each todo done line 28
#             # new_todos = [item.strip("\n") for item in todos]
#
#             for index, item in enumerate(todos):
#                 item = item.strip("\n")
#                 print(f"{index + 1} - {item}")
#         case "edit":
#             number = int(input("Number of todo to edit: "))
#
#             with open("todos.txt", "r") as file:
#                 todos = file.readlines()
#
#             new_todo = input("Enter new todo: ")
#             todos[number - 1] = new_todo + "\n"
#
#             with open("todos.txt", "w") as file:
#                 file.writelines(todos)
#         case "complete":
#             number = int(input("Number of the todo to complete: "))
#
#             with open("todos.txt", "r") as file:
#                 todos = file.readlines()
#
#             index = number - 1
#             todo_to_remove = todos[index].strip("\n")
#             todos.pop(index)
#
#             with open("todos.txt", "w") as file:
#                 file.writelines(todos)
#
#             print(f"The todo '{todo_to_remove}' has been removed from the list")
#         case "exit":
#             break
#         case _:
#             print("You entered an unknown command")
# ##
