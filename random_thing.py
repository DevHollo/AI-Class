from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.title("test hi")
root.geometry(f"{root.winfo_screenwidth()//2}x{root.winfo_screenheight()//2}")

def hi():
    for i in range(6320):
        if i % 2 == 0:
            print('bye')
        elif i % 3 == 0:
            continue
        elif i % 5 == 0:
            print("hola")
        elif i % 10 == 0:
            print("bonjour")
        else:
            print("hi")

ttk.Label(root, text="Hi").pack()
ttk.Label(root, text=f"{root.winfo_screenwidth()//2}x{root.winfo_screenheight()//2}").pack(pady=5)
ttk.Button(root, text="hi", command=lambda: hi()).pack(padx=29, pady=29)

print("hi")
print(500 % 10)
root.mainloop()
