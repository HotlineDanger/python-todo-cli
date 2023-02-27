import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do")
add_button = sg.Button("Add")

window = sg.Window("My To-Do app", layout=[[label], [input_box, add_button]], font=("Helvetica", 20))
window.read()
print("Bye")
window.close()
