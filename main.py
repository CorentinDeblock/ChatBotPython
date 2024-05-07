from chatterbot import ChatBot
from threading import Thread
from shared import bot_name, database_uri, storage_adapter

import tkinter

chatbot = ChatBot(
    bot_name,
    storage_adapter=storage_adapter,
    database_uri=database_uri
)

def handle_command_keybind(event):
    handle_command()

def handle_command():
    text_input = input_box.get("1.0", tkinter.END)
    global thread_save

    if len(text_input) > 0:
        text.insert(tkinter.END,"Toi: " + text_input)
        text.insert(tkinter.END, f"{bot_name}: pense...\n")
        t = Thread(target=respond, args=[text_input])
        t.start()

def respond(text_input):
    bot_input = chatbot.get_response(text_input)
    text.delete("end-2l","end-1l")
    text.insert(tkinter.END, f"{bot_name}: {bot_input}")

root = tkinter.Tk()
root.configure(background="black")

def handle_keydown(event):
    if event.keysym == "Return" and event.state != 9:
        handle_command()
        return "break"

text = tkinter.Text(
    root, 
    width=100, 
    bg="black",
    fg="white",
    height=20
)

input_box = tkinter.Text(
    root, 
    width=81, 
    bg="black",
    fg="white",
    height=5
)

input_box.bind("<KeyPress>", handle_keydown)

button = tkinter.Button(
    root, 
    width=20, 
    height=5,
    bg="black",
    fg="white",
    command=handle_command, 
    text="ask"
)

text.grid(row=0, column=0)
input_box.grid(row=1, column=0, sticky=tkinter.W)
button.grid(row=1, column=0, sticky=tkinter.E)

root.mainloop()