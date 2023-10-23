import tkinter as tk
from tkinter import messagebox

# Roma rakamlarını çeviren bir fonksiyon
def roman_to_arabic(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabic = 0
    prev_value = 0

    for letter in reversed(roman):
        if letter not in roman_dict:
            raise ValueError("Geçersiz Roma Rakamı")
        if roman_dict[letter] >= prev_value:
            arabic += roman_dict[letter]
        else:
            arabic -= roman_dict[letter]
        prev_value = roman_dict[letter]

    return arabic

# Arayüz için çevirme fonksiyonu
def convert():
    roman_numeral = entry.get()
    try:
        arabic_numeral = roman_to_arabic(roman_numeral)
        result_label.config(text=f"{roman_numeral} = {arabic_numeral}")
    except ValueError as e:
        messagebox.showerror("Hata", str(e))

# Ana Tkinter penceresi oluşturma
window = tk.Tk()
window.title("Roma Rakamı Dönüştürücü")
window.geometry("400x350")  # Pencere boyutunu ayarla
window.configure(bg="lightgray")  # Pencere arkaplan rengini ayarla

# Giriş kutusu
entry_label = tk.Label(window, text="Roma Rakamı Girin:", font=("Arial", 12))
entry_label.pack()

entry = tk.Entry(window, font=("Arial", 12))
entry.pack()

# Çevirme düğmesi
convert_button = tk.Button(window, text="Çevir", command=convert, bg="darkgrey", fg="black", font=("Arial", 12))
convert_button.pack()

# Sonuç etiketi
result_label = tk.Label(window, text="", bg="lightgrey", font=("Arial", 14))  # Etiket arkaplan rengini ayarla
result_label.pack()

# Tablo başlığı
table_label = tk.Label(window, text="Roma Rakamı - Arap Rakamı Tablosu", font=("Arial", 14))
table_label.pack()

# Tabloyu oluşturmak için bir çerçeve kullanabilirsiniz
table_frame = tk.Frame(window)
table_frame.pack()

# Tabloyu oluşturun
table = tk.Label(table_frame, text="Roma Rakamı", font=("Arial", 12), padx=10, borderwidth=1, relief="solid")
table.grid(row=0, column=0)

arabic_label = tk.Label(table_frame, text="Arap Rakamı", font=("Arial", 12), padx=10, borderwidth=1, relief="solid")
arabic_label.grid(row=0, column=1)

# Tablo verilerini ekleyin
data = [
    ("I", 1),
    ("V", 5),
    ("X", 10),
    ("L", 50),
    ("C", 100),
    ("D", 500),
    ("M", 1000)
]

for i, (roman, arabic) in enumerate(data, start=1):
    roman_label = tk.Label(table_frame, text=roman, font=("Arial", 12), padx=10, borderwidth=1, relief="solid")
    roman_label.grid(row=i, column=0)

    arabic_label = tk.Label(table_frame, text=arabic, font=("Arial", 12), padx=10, borderwidth=1, relief="solid")
    arabic_label.grid(row=i, column=1)




# Ana döngüyü başlatma
window.mainloop()
