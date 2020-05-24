import random
import tkinter as tk
import pandas as pd
import datetime


def CheckLove():
    global result
    text_area = tk.Text(master=root, height=2, width=60, bg="#FFFF99")
    text_area.grid(columnn=0, row=5)
    result = ("Уровень любви: ", result)
    text_area.insert(tk.END, result)


root = tk.Tk()
root.geometry('400x300')
root.title('Калькулятор любви к Юре')
result = 40 + int(pd.datetime.now().second)

entryname1 = tk.Entry(root, width=20, )
entryname1.grid(column=1, row=1)
entryname2 = tk.Entry(root, width=20)
entryname2.grid(column=1, row=2)

button2 = tk.Button(text="   ПРОВЕРЬ УРОВЕНЬ ЛЮБВИ К ЮРЕ   ", bg='pink', command=CheckLove)
button2.grid(column=1, row=3)

label1 = tk.Label(root, text='Введи Имя : ', bg='red', font=('', 15, 'bold'))
label1.grid(row=1, column=0, pady=5, padx=5)

label2 = tk.Label(root, text='Friends Name: ', bg='red', font=('', 15, 'bold'))
label2.grid(row=2, column=0, pady=5, padx=5)

root.mainloop()
