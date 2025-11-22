from tkinter import *

#window
window = Tk()
window.title("BMI")
window.minsize(100, 100)
window.config(padx=20, pady=20)

weight_label = Label(text="Enter your Weight(kg)")
weight_label.config(fg="black", font=("Arial", 10))
weight_label.pack()


weight_entry = Entry(width=20)
weight_entry.config(fg="black", font=("Arial", 10))
weight_entry.focus()
weight_entry.pack()

height_label = Label(text="Enter Your Height(cm)")
height_label.config(fg="black", font=("Arial", 10))
height_label.pack()

height_entry = Entry(width=20)
height_entry.config(fg="black", font=("Arial", 10))
height_entry.pack()



def calculate_bmi():
    weight = int(weight_entry.get())
    height = int(height_entry.get())
    height = (height / 100)
    bmi = weight / (height * height)
    result_text = f"Your BMI is: {bmi:.2f} and it is {writeBmi(bmi)}"
    bmi_label.config(text=result_text)
bmi_button = Button(text="Calculate", command=calculate_bmi)
bmi_button.pack()

bmi_label = Label(text= "")
bmi_label.pack()

weight_entry.bind("<Return>", lambda event: height_entry.focus())
height_entry.bind("<Return>", lambda event: bmi_button.invoke())

def writeBmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        return "Normal"
    elif bmi >= 25 and bmi <= 39.9:
        return "Overweight"
    else:
        return "Obese"






window.mainloop()