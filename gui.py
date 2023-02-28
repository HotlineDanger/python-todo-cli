import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do app",
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    print("Bye")
    match event:
        case "Add":

window.close()
