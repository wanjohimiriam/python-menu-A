from tkinter import Toplevel, Button, Tk, Menu
top = Tk()
menubar = Menu(top)
file = Menu(menubar, tearoff=0)
file.add_command(label="New")
file.add_command(label="Save")
file.add_command(label="Save As")
file.add_command(label="Open")
file.add_command(label="Close")
file.add_separator()
file.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="file", menu=file)
edit = Menu(menubar, tearoff=1)
edit.add_command(label="undo")
edit.add_separator()
edit.add_command(label="ut")
edit.add_command(label="copy")
edit.add_command(label="paste")
edit.add_command(label="delete")
edit.add_command(label="select all")
menubar.add_cascade(label="Edit", menu=edit)
help = Menu(menubar, tearoff=0)
help.add_command(label="Absent")
menubar.add_cascade(label="Help", menu=help)
view = Menu(menubar, tearoff=0)
view.add_command(label="Appearance")
view.add_command(label="Tools")
view.add_command(label="Run")
view.add_command(label="Zoom")
menubar.add_cascade(label="View", menu=view)
top.config(menu=menubar)
top.mainloop()






