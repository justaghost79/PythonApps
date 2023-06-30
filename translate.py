import tkinter as tk
from tkinter.ttk import Notebook

class Translate (tk.Tk):
    def translate():
        print("Translate")
        
    def __init__(self):



        super().__init__()

        self.title("Translate")
        self.notebook = Notebook(self)
        self.notebook.pack(fill = tk.BOTH, expand = 1)

        english_tab = tk.Frame(self.notebook)
        self.english_entry = tk.Text(english_tab)
        self.english_entry.pack(side = tk.TOP, expand=1)
        
        self.translate_button = tk.Button(english_tab, text="Translate", command = self.translate)
        self.translate_button.pack(side= tk.BOTTOM, fill = tk.X)

        self.notebook.add(english_tab, text = "English")

if __name__ == "__main__":
    translate = Translate()
    translate.mainloop()
