import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()


def addApp():
    filename= filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack()
frame = tk.Frame(root,bg="white")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
openFile = tk.Button(root, text="Open File", padx=15,
                     pady=10, fg="white", bg="maroon" ,command=addApp)
openFile.pack()
runApps = tk.Button(root, text="Run Apps", padx=15,
                     pady=10, fg="white", bg="maroon")

runApps.pack()
root.mainloop()
