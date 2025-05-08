import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

def sacuvaj_trosak():
    datum = entry_datum.get()
    naziv = entry_naziv.get()
    iznos = entry_iznos.get()

    if not datum or not naziv or not iznos:
        messagebox.showwarning("Greška", "Sva polja moraju biti popunjena.")
        return

    try:
        iznos = float(iznos)
        with open("troskovi.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([datum, naziv, iznos])
        messagebox.showinfo("Uspeh", "Trošak sačuvan.")
        entry_datum.delete(0, tk.END)
        entry_naziv.delete(0, tk.END)
        entry_iznos.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Greška", "Iznos mora biti broj.")

app = tk.Tk()
app.title("Lični troškovi")

tk.Label(app, text="Datum (YYYY-MM-DD):").pack()
entry_datum = tk.Entry(app)
entry_datum.pack()
entry_datum.insert(0, datetime.today().strftime('%Y-%m-%d'))

tk.Label(app, text="Naziv troška:").pack()
entry_naziv = tk.Entry(app)
entry_naziv.pack()

tk.Label(app, text="Iznos (€):").pack()
entry_iznos = tk.Entry(app)
entry_iznos.pack()

tk.Button(app, text="Sačuvaj trošak", command=sacuvaj_trosak).pack(pady=10)

app.mainloop()
