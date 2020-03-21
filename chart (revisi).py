import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('WELCOME TO CHART MAKER :)')
Country = []
Total= []

def input():
    try:
        if len(Country) == 0:
            name_country1 = name_country.get()
            name1 = name_country1.split(',')
            for i in name1:
                Country.append(i)
            Total1 = total_sufferer.get()
            Total2 = Total1.split(",")
            Total3 = [int(i) for i in Total2]
            for x in Total3:
                Total.append(x)
    except:
        messagebox.showwarning('WARNING !', 'DATA INPUT MUST BE COMPLETED AND IN PAIRS !')
        return
    x = range(len(Country))
    if a.get() == 1:
        plt.bar(x, Total)
        plt.xticks(x, Country)
        plt.xlabel('NAME OF COUNTRY')
        plt.ylabel('TOTAL SUFFERER COVID-19')
        plt.title('BAR CHART SUFFERER COVID-19')
        plt.show()
    else:
        plt.plot(x, Total)
        plt.xticks(x, Country)
        plt.xlabel('NAME OF COUNTRY')
        plt.ylabel('TOTAL SUFFERER COVID-19')
        plt.title('LINE CHART SUFFERER COVID-19')
        plt.show()
    return

def reload():
    name_country.delete(0, END)
    total_sufferer.delete(0, END)
    a = []
    if len(Country) > 0 & len(Total) > 0:
        b = Country.pop()
        c = Total.pop()
        a.append(b)
        a.append(c)
        a.remove(b)
        a.remove(c)
    return

label= Label(root, text='NAME OF COUNTRY : ').grid(row=0, column=0, sticky=E, pady=2)
label1 = Label(root, text='TOTAL SUFFERER COVID-19 : ').grid(row=1, column=0, pady=2)
name_country = Entry(root, width=75)
name_country.grid(row=0, column=1, padx=5)
total_sufferer = Entry(root, width=75)
total_sufferer.grid(row=1, column=1, padx=5)
a = IntVar()
bar = Radiobutton(root, text="BAR CHART", variable=a, value=1)
bar.grid(row=2, column=1, sticky=W)
line = Radiobutton(root, text="LINE CHART", variable=a, value=2)
line.grid(row=3, column=1, sticky=W)
button1 = Button(root, text='APPEAR', width=10, command=input).grid(row=5, column=1, sticky=E, padx=4)
button2 = Button(root, text='RELOAD', width=10, command=reload).grid(row=5, column=2, sticky=E, padx=4)

root.mainloop()