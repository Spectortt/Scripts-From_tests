import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.first_name_label = tk.Label(self, text="First Name:")
        self.first_name_label.pack(side="top")
        self.first_name_entry = tk.Entry(self)
        self.first_name_entry.pack(side="top")

        self.last_name_label = tk.Label(self, text="Last Name:")
        self.last_name_label.pack(side="top")
        self.last_name_entry = tk.Entry(self)
        self.last_name_entry.pack(side="top")

        self.show_button = tk.Button(self)
        self.show_button["text"] = "Show"
        self.show_button["command"] = self.show_full_name
        self.show_button.pack(side="top")

        self.full_name_label = tk.Label(self, text="")
        self.full_name_label.pack(side="top")

    def show_full_name(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        full_name = f"{first_name} {last_name}"
        self.full_name_label["text"] = full_name

root = tk.Tk()
app = Application(master=root)
app.mainloop()