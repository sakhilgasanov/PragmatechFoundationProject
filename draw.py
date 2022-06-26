import tkinter as tk
pencere=tk.Tk()
def giris():
    
    etiket=tk.Label(text='Esas ekran')
    etiket.pack()
    if #you click the giris button then new window opens
girish=tk.Button(text='giris edin')
girish.pack()

def cixis():
     etiket['text']='Gorusenedek'
     duyme['text']='Gozleyin'
     duyme['state']='disabled'
     pencere.after(2000, pencere.destroy)
     


duyme=tk.Button(text='cixis', command=cixis)
duyme.pack()

pencere.protocol('WM_DELETE_WINDOW', cixis)

pencere.mainloop()