from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Diet_calculator")

# la taille
label1 = Label(root, text="Votre taille en cm")
size = Entry(root, width=25)

label2 = Label(root, text="Votre poid en kg")
weigth = Entry(root, width=25)

label3 = Label(root, text="Votre age")
Age = Entry(root, width=25)

label4 = Label(root, text="Votre sexe")

label1.grid(row=1,column=0, pady=5, padx=5)
size.grid(row=1,column=1, columnspan=2, pady=5, padx=5)

label2.grid(row=2, column=0, pady=5, padx=5)
weigth.grid(row=2,column=1, columnspan=2, pady=5, padx=5)

label3.grid(row=3, column=0, pady=5, padx=5)
Age.grid(row=3,column=1, columnspan=2, pady=5, padx=5)

radio_var = StringVar()
label4.grid(row=4, column=0, pady=5, padx=5)
radio_buttons1 = Radiobutton(root, text="male", variable=radio_var, value="male")
radio_buttons2 = Radiobutton(root, text="femele", variable=radio_var, value="femele")
radio_buttons1.grid(row=4, column = 1, pady=5, padx=5)
radio_buttons2.grid(row=4, column = 2, pady=5, padx=5)

button_1 = Button(root,text="Calcule du poid idéal", padx=30, pady=10)
button_2 = Button(root,text="Calcule de IMC", padx=40, pady=10)
button_3 = Button(root,text="Clear", padx=20, pady=10)
button_4 = Button(root,text="Quit", command= quit , padx=23, pady=10)
button_calcule_cal = Button(root,text="Calories recommandé/jours", padx=13, pady=10)

button_1.grid(row=5, column=0, padx=5, pady=5)
button_2.grid(row=5, column=1, columnspan=2, padx=5, pady=5)
button_calcule_cal.grid(row=6, column=0 ,padx=5, pady=5)
button_3.grid(row=6, column=1, padx=5, pady=5)
button_4.grid(row=6, column=2, padx=5, pady=5)

root.mainloop()