from tkinter import*
import os



def go(data):
    for _ in os.listdir():
        if data == _:
            os.chdir(os.getcwd() + "\\" + data)
    if data == "...":
        tmp = os.getcwd()
        while True:
            if tmp[-1] == "\\":
                break
            else:
                tmp = tmp[:-1]
        os.chdir(tmp)
        go("mostrar")
        
            


    
    if data == "ver":
        aa["text"]=os.getcwd()
        aa.pack()
    if data == "mostrar":
        b = ""
        for _ in os.listdir():
            b = b + "\n" + _
        bb["text"]=b
        bb.pack(ipadx=2)
    
    










w = Tk()


com = Entry()
com.pack(side="left")
bot = Button(text="go", command=lambda:go(com.get())).pack(side="right")
aa = Label()
bb = Label()

mainloop()
