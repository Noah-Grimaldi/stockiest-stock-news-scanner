import runpy
import tkinter as tk


root = tk.Tk()


def start_filter():
    runpy.run_module(mod_name='main.py')


def stop_filter():
    # this is braindead
    not runpy.run_module(mod_name='main.py')


canvas = tk.Canvas(root, height=700, width=700, bg='#263D42')
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

display = tk.Message(root, text='test')
display.pack()

openFile = tk.Button(root, text='Start Filter', padx=10, pady=5, fg='white', bg='#263D42', command=start_filter)
openFile.pack()

runApps = tk.Button(root, text='Stop Filter', padx=10, pady=5, fg='white', bg='#263D42', command=stop_filter)
runApps.pack()

root.mainloop()
