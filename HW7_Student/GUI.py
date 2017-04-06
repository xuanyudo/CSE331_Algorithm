import tkinter
from tkinter import *
import os
from tkinter import filedialog

class Application(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.outputBox = Text(bg='black', fg='green', relief=SUNKEN, yscrollcommand='TRUE')
        self.outputBox.pack(fill='both', expand=True)
        self.button1 = Button(self, text='button1', width=40, bg ='black', fg='green', activebackground='black', activeforeground='green')
        self.button1.pack(side=RIGHT, padx=5, pady=5)
        self.button2 = Button(self, text='button2', width=20, bg='black', fg='green', activebackground='black', activeforeground='green')
        self.button2.pack(side=LEFT, padx=5, pady=5)

def main():
    root = Tk()
    root.geometry('1100x350+500+300')
    # root.configure(background = 'black')
    app = Application(root)
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(filetypes=(("All files","*.*"),("png","*.png")))
    print ("You chose %s" % tempdir)

    root.mainloop()
if __name__ == '__main__':
    main()
