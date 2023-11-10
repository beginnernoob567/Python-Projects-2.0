import tkinter
from tkinter import *
from textblob import TextBlob

root=Tk()

root.title('Spelling Checker')

root.geometry("700x400")

root.config(background="#dae6f6")

def clear():

    cs.destroy()
    button1['state']=NORMAL

def check_spelling():

    button1['state']=DISABLED
    word=enter_text.get()
    a=TextBlob(word)
    global cs

    if word!=a.correct():

        right=str(a.correct())
        cs=Label(root,text="correct text is: "+str(a.correct()),font=("poppins",20),bg="#dae6f6",fg="#364971")
        cs.place(x=100,y=275)

    else:
        
        cs=Label(root,text="You have entered the correct Word",font=("poppins",20),bg="#dae6f6",fg="#364971")
        cs.place(x=100,y=275)


        
heading=Label(root,text='Spelling Checker',font=("Trebuchet MS",30,"bold"),bg='#dae6f6',fg='#364871')
heading.pack(pady=50)

enter_text=Entry(root,justify="center",width=30,font=("poppins",25),bg="white",border=2)
enter_text.pack(pady=10)
enter_text.focus()

button1=Button(root,text="Check",font=("arial",20,"bold"),fg="white",bg="red",command=check_spelling)
button1.place(x=225,y=225)

button2=Button(root,text="Clear",font=("arial",20,"bold"),fg="white",bg="red",command=clear)
button2.place(x=335,y=225)



root.mainloop()
