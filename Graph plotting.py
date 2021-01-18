import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

window = Tk()
canvas = Canvas(window, width = 400, height = 600)
canvas.pack()

x_label = Label(window, text = 'Values of \'x\' (Comma seperated):')
canvas.create_window(200, 30, window = x_label)
x_values = Entry(window)
canvas.create_window(200, 50, window = x_values)

y_label = Label(window, text = 'Values of \'y\' (Comma seperated):')
canvas.create_window(200, 80, window = y_label)
y_values = Entry(window)
canvas.create_window(200, 100, window = y_values)

deg_label = Label(window, text = 'Enter the degree of polynomial to be fitted:')
canvas.create_window(200, 1200, window = deg_label)
deg_val = Entry(window)
canvas.create_window(200, 150, window = deg_val)

def PlotGraph():
    x = x_values.get()
    x = x.split(',')
    x = list(eval(i) for i in x)

    y = y_values.get()
    y = y.split(',')
    y = list(eval(j) for j in y)

    deg = deg_val.get()
    deg = int(deg)

    poly = np.poly1d(np.polyfit(x, y, deg))
    x1 = np.linspace(min(x), max(x), 200)
    y1 = poly(x1)

    plt.plot(x1, y1)
    plt.scatter(x, y)
    plt.grid()
    plt.show()

plot_button = Button(text = 'Plot the graph', command = PlotGraph)
canvas.create_window(200, 180, window = plot_button)

window.mainloop()