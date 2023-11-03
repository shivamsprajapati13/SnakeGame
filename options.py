from time import sleep
import os

from tkinter import Tk, Label, Radiobutton, StringVar, Button, messagebox, Frame


def on_enter(e):
    b1['background'] = '#033500'
    b1['foreground'] = 'white'


def on_leave(e):
    b1['background'] = '#3cb043'
    b1['foreground'] = 'black'

def chooseOptions():
	if screenVal.get() == 'NA':
		messagebox.showinfo('Message','Select Your Option')
	else:
		if screenVal.get() == 'restart':
			root.withdraw()
			os.system('snakegame.py')

		elif screenVal.get() == 'resume':
			pass

		elif screenVal.get() == 'quit':
			root.withdraw()
			quit()

root = Tk()
root.geometry("300x200")
root.title("Snake")
root.resizable(False,False)


Label(root,text = "Select Your Options",font='consolas 14 bold').grid(row = 1, column = 2)

screenVal = StringVar()
screenVal.set('NA')
r1 = Radiobutton(root,text = "Start",variable = screenVal,value = 'restart',font='consolas 14 bold').grid(row = 5,column = 2)
# r2 = Radiobutton(root,text = "Resume",variable = screenVal,value = 'resume',font='consolas 14 bold').grid(row = 8,column = 2)
r3 = Radiobutton(root,text = "Quit",font='consolas 14 bold',variable = screenVal,value = 'quit').grid(row = 11,column = 2)



b1 = Button(root, text = 'Submit',cursor = 'hand2',font='consolas 14 bold',command = chooseOptions)
b1.bind("<Enter>", on_enter)
b1.bind("<Leave>", on_leave)
b1.grid(row = 15,column = 2)


root.mainloop()