from tkinter import *
from tkinter import messagebox as mb
from find_answers import *


root = Tk()
root.title("Найти ответы")
qw = Label(text="Вопрос")
ent = Entry(root, width=100)
qw.grid(column=0, row=0)
ent.grid(column=0, row=1)


asw = Label(text="Варианты")
asw.grid(column=0, row=2)
answers = Text(root,width=100) 
answers.grid(column=0, row=3)

#Здесь просто код для работы копипасты
#-------------------------------------
editmenu = Menu(tearoff=0)
editmenu.add_command(label="Cut", \
                     accelerator="Ctrl+X", \
                     command=lambda: \
                             self.editor.event_generate('<<Cut>>'))
editmenu.add_command(label="Copy", \
                     accelerator="Ctrl+C", \
                     command=lambda: \
                             self.editor.event_generate('<<Copy>>'))
editmenu.add_command(label="Paste", \
                     accelerator="Ctrl+V", \
                     command=lambda: \
                             self.editor.event_generate('<<Paste>>'))
#--------------------------------------

def find_answers():
    qwst1 = ent.get()
    answ1 = answers.get("1.0",'end-1c')
    ts = TestSolver(qwst1,answ1)
    res= ts.get_answers()
    mb.showinfo(title="Ответы",message=res)
    res = None
def clear():
    print(answers)

btn1 = Button(text="Найти", width=10,height=2, command=find_answers)
btn1.grid(column=0, row=4)

btn2 = Button(text="Очистить", width=10,height=2, command=clear)
btn2.grid(column=1, row=4)

root.mainloop()