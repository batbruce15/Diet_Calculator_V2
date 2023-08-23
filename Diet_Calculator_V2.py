from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Diet_calculator")

# functions field
def clear():
    size.delete(0,END)
    weigth.delete(0,END)
    Age.delete(0,END)

def calcule_calories():
    sexe = radio_var.get()
    poid = float(weigth.get())
    tail = float(size.get())
    age = int(Age.get())
    if(sexe == "male"):
        MB = 88.362 + (13.397 * poid) + (4.799 * tail) - (5.677 * age)
        messagebox.showinfo(round(MB,0))
    else:
        MB = 88, 362 + (13.397 * poid) + (4.799 * tail) - (5.677 * age)
        messagebox.showinfo(round(MB,0))

def Compute_The_IMC_Indicator():
    tail = int(size.get())/100
    poid = int(weigth.get())
    IMC = poid / (tail*tail)
    messagebox.showinfo(f"IMC = {round(poid/(tail*tail),2)}")
    if(IMC < 18.5):
        message = "Vous etes en sous-poid, ce qui peut indiquer un manque de nutriments et une possible insuffisance pondérale."
        chunks = [message[i:i + 50] for i in
                  range(0, len(message), 50)]  # Découper le message en parties de 50 caractères

        formatted_message = "\n".join(chunks)
        messagebox.showwarning("Avertissement", formatted_message)
    elif(IMC>18.5 and IMC<24.9):
        message = "Poid corporel normal, vous en bonne santé"
        chunks = [message[i:i + 50] for i in
                  range(0, len(message), 50)]  # Découper le message en parties de 50 caractères

        formatted_message = "\n".join(chunks)
        messagebox.showinfo("Bravo", formatted_message)
    elif(IMC>24.9 and IMC<30):
        message = "Vous etes en surpoid, cela peut augmenter le risque de problèmes de santé tels que le diabète de type 2, l'hypertension artérielle et les maladies cardiaques."
        chunks = [message[i:i + 50] for i in
                  range(0, len(message), 50)]  # Découper le message en parties de 50 caractères

        formatted_message = "\n".join(chunks)
        messagebox.showwarning("Avertissement", formatted_message)
    else:
        message = "Obésité, ce qui peut accroître considérablement le risque de divers problèmes de santé graves, y compris les maladies cardiovasculaires, le diabète, les troubles articulaires, etc."
        chunks = [message[i:i + 50] for i in
                  range(0, len(message), 50)]  # Découper le message en parties de 50 caractères

        formatted_message = "\n".join(chunks)
        messagebox.showwarning("Danger", formatted_message)
#end of functions field
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
button_2 = Button(root,text="Calcule de IMC", padx=40, pady=10, command=Compute_The_IMC_Indicator)
button_3 = Button(root,text="Clear", padx=20, pady=10, command=clear)
button_4 = Button(root,text="Quit", command= quit , padx=23, pady=10)
button_calcule_cal = Button(root,text="Calories recommandé/jours", padx=13, pady=10, command=calcule_calories)

button_1.grid(row=5, column=0, padx=5, pady=5)
button_2.grid(row=5, column=1, columnspan=2, padx=5, pady=5)
button_calcule_cal.grid(row=6, column=0 ,padx=5, pady=5)
button_3.grid(row=6, column=1, padx=5, pady=5)
button_4.grid(row=6, column=2, padx=5, pady=5)



root.mainloop()