from tkinter import *
import random
import ctypes
import tkinter as tk
root = Tk()
root.title('PANDA TYPE')
root.option_add('*Font','Times')
root.geometry('800x700')
root.iconbitmap("new.ico")
root.configure(bg="#5d8aa8")
root.minsize(width=1100,height=654)
photo = PhotoImage(file = r"C:\Users\soods\OneDrive\Documents\Github\typing project\starte.png")
photo2 = PhotoImage(file = r"C:\Users\soods\OneDrive\Documents\Github\typing project\about.png")
def about():
    top = Toplevel()
    top.geometry('500x300')
    top.iconbitmap("new.ico")
    top.minsize(width=600,height=400)
    top.maxsize(width=600,height=400)
    top.title('ABOUT THE PROGRAM')
    top.configure(bg="#CCEEFF")
    d = Label(top,text = 'Hey, Welcome to our Program',bg="#CCEEFF",fg="black").pack()
    bt1 = Button(top,text = 'CLOSE WINDOW',padx = 40, pady = 20,command = top.destroy,bg="#CCEEFF",fg="black").place(x=353,y=324)
    l1=Label(top,)

def start():

    top = Toplevel()
    top.geometry('600x400')
    top.minsize(width=300,height=200)
    top.title('LET START THE TEST')
    top.iconbitmap("new.ico")
    
    
    frame2 = Label(top,text ="LET'S BEGIN",padx = 10,pady = 10,font=("consolas 18 bold"),bg='red',fg='black').pack()
    canvas = Canvas(top, width= 2000, height= 2000, bg="grey").pack()
    bt2 = Button(top,text = 'CLOSE WINDOW',padx = 15, pady = 10,command = top.destroy).place(relx=0.7,rely=0.8) 
    
    top.option_add("*Label.Font", "consolas 30")
    top.option_add("*Button.Font", "consolas 30")

    def keyPress(event=None):
        try:
            if event.char.lower() == labelRight.cget('text')[0].lower():
                labelRight.configure(text=labelRight.cget('text')[1:])
                labelLeft.configure(text=labelLeft.cget('text') + event.char.lower())
                currentLetterLabel.configure(text=labelRight.cget('text')[0])
        except tk.TclError:
            pass
    
    def resetWritingLabels():
        possibleTexts = [
            'A late 20th century trend in typing, primarily used with devices with small keyboards (such as PDAs and Smartphones), is thumbing or thumb typing. This can be accomplished using one or both thumbs. Similar to desktop keyboards and input devices, if a user overuses keys which need hard presses and/or have small and unergonomic layouts, it could cause thumb tendonitis or other repetitive strain injury.',
            'Engineers, as practitioners of engineering, are people who invent, design, analyze, build, and test machines, systems, structures and materials to fulfill objectives and requirements while considering the limitations imposed by practicality, regulation, safety, and cost. The work of engineers forms the link between scientific discoveries and their subsequent applications to human and business needs and quality of life.',
            'A virtual assistant (typically abbreviated to VA) is generally self-employed and provides professional administrative, technical, or creative assistance to clients remotely from a home office.'
        ]
        text = random.choice(possibleTexts).lower()
        splitPoint = 0
        global labelLeft
        labelLeft = Label(top, text=text[0:splitPoint], fg='grey')
        labelLeft.place(relx=0.5, rely=0.5, anchor=E)

        global labelRight
        labelRight = Label(top, text=text[splitPoint:])
        labelRight.place(relx=0.5, rely=0.5, anchor=W)

        global currentLetterLabel
        currentLetterLabel = Label(top, text=text[splitPoint], fg='grey')
        currentLetterLabel.place(relx=0.5, rely=0.6, anchor=N)

        global timeleftLabel
        timeleftLabel = Label(top, text=f'0 Seconds', fg='grey')
        timeleftLabel.place(relx=0.5, rely=0.4, anchor=S)

        global writeAble
        writeAble = True
        top.bind('<Key>', keyPress)

        global passedSeconds
        passedSeconds = 0

        top.after(60000, stopTest)
        top.after(1000, addSecond)


    def stopTest():
        global writeAble
        writeAble = False
        
        amountWords = len(labelLeft.cget('text').split(' '))
        
        timeleftLabel.destroy()
        currentLetterLabel.destroy()
        labelRight.destroy()
        labelLeft.destroy()

        global ResultLabel
        ResultLabel = Label(top, text=f'Words per Minute: {amountWords}', fg='black')
        ResultLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

        global ResultButton
        ResultButton = Button(top, text=f'Retry', command=restart)
        ResultButton.place(relx=0.5, rely=0.6, anchor=CENTER)

    def restart():
        ResultLabel.destroy()
        ResultButton.destroy()

        resetWritingLabels()

    def addSecond():

        global passedSeconds
        passedSeconds += 1
        timeleftLabel.configure(text=f'{passedSeconds} Seconds')

        if writeAble:
            top.after(1000, addSecond)

    resetWritingLabels()



c = tk.Label(root,text = '           TYPING SPEED TEST  ',font=('Arial','30'),bg="#5d8aa8",fg="white",bd='12')
a = Button(root,text = 'START', padx = 20 ,pady = 20,command = start,image=photo ) 
b = Button(root,text = 'ABOUT', padx = 20 ,pady = 20,command = about,image=photo2 )

a.place(x =90, y =150)
b.place(x =450, y =150)
c.place(x =90, y =70)


l1=Label(root,text="START",font=("Arial 25"),bg="#5d8aa8",fg="white").place(x=160,y=375)
l1=Label(root,text="ABOUT",font=("Arial 25"),bg="#5d8aa8",fg="white").place(x=515,y=375)



root.mainloop()