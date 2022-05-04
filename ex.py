import tkinter as tk
class Pencere(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol('WM_DELETE_WINDOW', self.cixis)
        self.etiket=tk.Label(text='esas ekran')
        self.etiket.pack()
        self.duyme=tk.Button(text='klikleyin')
        self.duyme.pack()
        
    def cixis(self):
        self.etiket['text']='gorusenedek'
        self.duyme['text']='gozleyin'
        self.duyme['state']='disabled'
        self.after(1000, self.destroy)

pencere=Pencere()
pencere.mainloop()