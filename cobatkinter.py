from tkinter import *

mainn = Tk()
mainn.geometry('400x150')

framing = LabelFrame(mainn,padx=20,pady=5)
framing.place(x=20,y=45)

def yoi():
    edG.delete(0,END)
    edP.delete(0,END)
    edF.delete(0,END)
    if entry1.get().isdigit() and int(entry1.get())>0:
        class mencari:
            def __init__(self,cari_nich):
                self.cari2 = cari_nich

            def keluaran(self):

                def deretGenap(p):
                    genap = [str(2*i) for i in range(1,p+1)]
                    return ','.join(genap)

                def deretPrima(q):
                    prima = []
                    possiblePrime = 2
                    while len(prima) < q:
                        faktor = []
                        for i in range(1,possiblePrime+1):
                            if possiblePrime % i == 0:
                                faktor.append(i)
                        if len(faktor) == 2:
                            prima.append(str(possiblePrime))
                        possiblePrime += 1    
                    return ','.join(prima)

                def fibonnaci(r):
                    if r == 1:
                        return '1'
                    elif r == 2:
                        return '1,1'
                    elif r > 2:
                        out = ['1','1']
                        ppq = 2
                        while len(out) < r:
                            out.append(str(int(out[ppq-1])+int(out[ppq-2])))
                            ppq += 1
                        return ','.join(out)

                edG.insert(0,deretGenap(int(self.cari2)))
                edP.insert(0,deretPrima(int(self.cari2)))
                edF.insert(0,fibonnaci(int(self.cari2)))
        cari = mencari(entry1.get())
        cari.keluaran()

    else:
        pass
            
tulis1 = Label(mainn, text = 'Counter').place(x=40,y=10)
entry1 = Entry(mainn, width=8)
entry1.place(x=134,y=10)
tombol1 = Button(mainn, text = 'Tampilkan Deret',width=23,command=yoi).place(x=195,y=10)

dG = Label(framing,text='Deret Genap').grid(row=0,column=0,sticky=W)
dGsp = Label(framing,text='',width=2).grid(row=0,column=1)
edG = Entry(framing, width=38)
edG.grid(row=0,column=2)
dP = Label(framing,text='Deret Prima').grid(row=1,column=0,sticky=W)
dPsp = Label(framing,text='',width=2).grid(row=1,column=1)
edP = Entry(framing, width=38)
edP.grid(row=1,column=2)
dF = Label(framing,text='Fibonacci').grid(row=2,column=0,sticky=W)
dFsp = Label(framing,text='',width=2).grid(row=2,column=1)
edF = Entry(framing, width=38)
edF.grid(row=2,column=2) 

mainn.mainloop()