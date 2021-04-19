# -*- coding: utf-8 -*-
from tkinter import *
import tkinter
import tkinter.messagebox

class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        # начальные значения, а так же отображение виджета Label
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
        self.lbl.place(x=11, y=50)

        # список кнопок для отображения
        btns = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "X^2"
        ]

        # рендер кнопок
        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFF", font=("Times New Roman", 15), command=com).place(x=x, y=y, width=115, height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

    # основная функция для выполнения логических операция
    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            self.formula = str((eval(self.formula))**2)
        elif operation == "=":
            # исключение, если пользователь делит число на ноль
            try:
                self.formula = str(eval(self.formula))
            except ZeroDivisionError:
                self.formula = ""
                tkinter.messagebox.showwarning(title="Error", message="You cannot divide by zero")
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    # возвращение в начальным значением
    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)

# создание окна калькулятора
if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("485x550+200+200")
    root.title("Calculator")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()