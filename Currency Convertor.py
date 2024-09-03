from tkinter import *
from requests import *

root = Tk()
root.geometry("400x250")
root.title("Currency Converter")
root.configure(bg='#f0f0f0')

f = ("Arial", 12, "bold")

def get_rate():
    try:
        url = 'https://api.exchangerate-api.com/v4/latest/GBP'
        res = get(url)
        data = res.json()
        inr_rate = data['rates']['INR']
        return 1 / inr_rate  
    except Exception as e:
        print("Error fetching data:", e)
        return None

def convert():
    try:
        amt_inr = float(entry_inr.get())
        rate = get_rate()
        if rate is not None:
            amt_gbp = amt_inr * rate
            label_res.config(text=f"{amt_inr} INR = {amt_gbp:.2f} GBP")
        else:
            label_res.config(text="Error fetching rate")
    except Exception as e:
        label_res.config(text="Error: " + str(e))

frame_input = Frame(root, bg='#f0f0f0')
frame_input.pack(pady=20)

label_inr = Label(frame_input, text="Enter Amount in INR:", font=f, bg='#f0f0f0')
entry_inr = Entry(frame_input, font=f, width=15)
btn_con = Button(root, text="Convert", command=convert, font=f, bg='#4CAF50', fg='white', relief=RAISED)
label_res = Label(root, font=f, bg='#f0f0f0')

label_inr.grid(row=0, column=0, padx=10)
entry_inr.grid(row=0, column=1, padx=10)
btn_con.pack(pady=10)
label_res.pack(pady=20)

root.mainloop()
