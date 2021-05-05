from tkinter import *
from math import e
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


def plot(a:int, b:int):
    b = b if b != 0 else 1
    y = [(a * e**(-1/(b*i)) ) if i != 0 else 1 for i in range(0,21)]
    plot1.plot(y)
    plot1.set_ylim([0, 100])
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack()


def slider1Action(self):
    global aValue
    global bValue
    bValue = 15 - int(slider1.get()) # get method to get value of slider
    # Removing previous results from graph
    plot1.clear()
    plot(aValue, bValue)
    # Appending the label if bValue is 0 or 80 or else
    if bValue == 0:
        slider1.config(label=labelRate+' (Worst)')
    elif bValue == 15:
        slider1.config(label=labelRate+' (Best)')
    else:
        slider1.config(label=labelRate)


def slider2Action(self):
    global aValue
    global bValue
    aValue = int(slider2.get())*0.5 + int(slider3.get())*0.5  # get method to get value of slider
    # Removing previous results from graph
    plot1.clear()
    plot(aValue,bValue)


def slider3Action(self):
    global aValue
    global bValue
    aValue = (int(slider2.get()) * 0.5) + (int(slider3.get()) * 0.5)  # get method to get value of slider
    # Removing previous results from graph
    plot1.clear()
    plot(aValue, bValue)


if __name__ == '__main__':
    global aValue
    global bValue
    aValue = 0
    bValue = 15
    root = Tk()
    root.geometry('500x500')
    labelRate = 'Prix'
    # slider 1 from 0 to 80 - step 10 setting slider1Action function with it
    slider1 = Scale(root, from_=0, to=15, length=200, label=labelRate+' (Worst)', width=20, resolution=5,
                    orient=HORIZONTAL,command=slider1Action)
    slider1.pack()
    # slider 1 from 0 to 40 - step 5 setting slider2Action function with it
    slider2 = Scale(root, from_=0, to=80, length=200, label='Recovery Rate', width=20, resolution=5,
                    orient=HORIZONTAL,command=slider2Action)
    slider2.pack()
    # slider 1 from 0 to 40 - step 5 setting slider3Action function with it
    slider3 = Scale(root, from_=0, to=80, length=200, label='Waning Immunity Rate', width=20, resolution=5,
                    orient=HORIZONTAL,command=slider3Action)
    slider3.pack()
    # Making figure of 5,5
    fig = Figure(figsize=(5, 5), dpi=100)
    plot1 = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master=root)
    # calling the plot function
    plot(aValue,bValue)
    root.mainloop()