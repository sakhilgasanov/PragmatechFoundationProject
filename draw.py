import tkinter as tk
pencere=tk.Tk()
def cixis():
     etiket['text']='Gorusenedek'
     duyme['text']='Gozleyin'
     duyme['state']='disabled'
     pencere.after(2000, pencere.destroy)
     
etiket=tk.Label(text='Esas ekran')
etiket.pack()

duyme=tk.Button(text='cixis', command=cixis)
duyme.pack()

pencere.protocol('WM_DELETE_WINDOW', cixis)

pencere.mainloop()