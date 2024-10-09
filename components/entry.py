import tkinter as tk

class Entry():
    def __init__(self, window, show_char=None, placeholder='') -> None:
        self.window = window
        self.show_char = show_char
        self.placeholder = placeholder
        self._changed = False

    def load(self):
        self.entered_text = tk.Entry(master=self.window)
        self.entered_text.bind('<Button-1>', self._clear_text)
        self.entered_text.pack(pady=5)
        self.entered_text.insert(0, self.placeholder)

    def get(self):
        return self.entered_text.get()

    def _clear_text(self, event):
        if not self._changed:
            self.entered_text.delete(0, len(self.entered_text.get()))
            self.entered_text['show'] = self.show_char
            self._changed = True
