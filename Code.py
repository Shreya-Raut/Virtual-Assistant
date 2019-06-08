import wikipedia 
import wolframalpha
from tkinter import *

root = Tk()

top_frame = Frame(root)
top_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side = BOTTOM)

label1 = Label(top_frame , text = "Question" )
nm = Entry(top_frame)

def printAnswer():
    try:
        answer = wikipedia.summary(nm)
    except:
        app_id = "XHX6TR-HV86KR8Y8G"
        client = wolframalpha.Client(app_id)
        re = client.query(nm)
        answer = next(re.results).text
    label2 = Label(bottom_frame , text = answer  ) 
    label2.pack(side = BOTTOM)
    
button1 = Button(top_frame , text = "search", command = printAnswer )
label1.pack(side = LEFT)
nm.pack(side = LEFT)
button1.pack(side = LEFT)

root.mainloop()