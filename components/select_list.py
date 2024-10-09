import tkinter as tk
from tkinter import messagebox, filedialog
from typing import List
from .select_item import SelectItem

class SelectList:
    def __init__(self, window, values) -> None:
        self.window = window
        self.values: List[SelectItem] = values

    def load(self):
        tk.Listbox
        self.lb = tk.Listbox(self.window, selectmode=tk.SINGLE, height=len(self.values), width=50)
        for v in self.values: self.lb.insert(tk.END, v)
        self.lb.pack()

    def callSelected(self) -> None:
        self.values[self.lb.curselection()[0]].call()

    def getSelected(self) -> SelectItem:
        return self.values[self.lb.curselection()[0]]
