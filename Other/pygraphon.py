import matplotlib.pyplot as plt
import customtkinter as ctk
from PIL import Image, ImageTk

x = []
y = []

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Graphon")
app.geometry("600x450")

label = ctk.CTkLabel(app, text="")
label.place(relx=0.5, rely=0.70, anchor="center")

def button1def():
    global x, y
    if (entry.get().isdigit and entry.get() != "") and (entry2.get().isdigit and entry2.get() != ""):
        x.append(int(entry.get()))
        y.append(int(entry2.get()))
        plt.plot(x, y, color="red", linewidth=2, marker="d")
        plt.title("График")
        plt.grid()
        plt.savefig("график.png")
        image = ImageTk.PhotoImage(Image.open("график.png"))
        label.configure(image=image)
        entry.delete(0, ctk.END)
        entry2.delete(0, ctk.END)

entry = ctk.CTkEntry(app, placeholder_text="x")
entry.pack(pady=10)

entry2 = ctk.CTkEntry(app, placeholder_text="y")
entry2.pack()


button = ctk.CTkButton(app, text="Додавання інформації", command=button1def)
button.place(relx=0.5, rely=0.35, anchor="center")



app.mainloop()