from tkinter import Label, Tk 
import time

app_window = Tk() 
app_window.title("Digital Clock") 
app_window.geometry("550x200") 

label1 = Label(app_window, font=('DS-DIGITAL', 70), background="black", foreground="cyan") 
label1.grid(row=1, column=1)

label2 = Label(app_window, font=("Boulder", 40, 'bold'), background="#ffbe0b", foreground="#5f0f40")
label2.grid(row=0, column=1)

def digital_date():
    date_live = time.strftime("%d %B, %Y")
    label2.config(text=date_live)
    label2.after(1000, digital_clock)

def digital_clock(): 
    time_live = time.strftime("%H:%M:%S %p")
    label1.config(text=time_live)
    label1.after(200, digital_clock)

digital_date()
digital_clock()
app_window.mainloop()