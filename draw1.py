import tkinter as tk

pencere=tk.Tk()
pencere.geometry('1000x300')

etiket=tk.Label(text='Esas ekran')
etiket.pack()

duyme=tk.Button(text='Klikleyin')
duyme.pack()

pencere.mainloop()
