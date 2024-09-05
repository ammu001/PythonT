import time
from googletrans import Translator
#from tkinter import *
import tkinter as tk
import csv

def callback():
    txtArea.delete(0.0,'end')
    txtArea.configure(state="normal")
    txtValue = nameEntered.get()
    print(txtValue)    
    data= csv.reader(open('tamilsyn.csv',encoding='utf-8'))    
    for row in data :
            myList =[]
            dot_split=""
            if (txtValue.lower()) in row[0] :                
                print(row[1] ,"in csv file", row[1])                                    
                dot_split = row[2]                                
                start = 0
                for i in range(len(dot_split)):
                    if dot_split[i] == ';':
                        print(dot_split[start:i])
                        start = i+1
                    print(dot_split[start:])
                    dot_split=dot_split + '\n'
                    
                #myList.append(dot_split)   
                break
            else :
                print(txtValue,"Not in csv file")
                out = translator.translate(txtValue,dest = "ta" )
                #myList.append(out.text)
                dot_split = out.text
            '''
            else:
                print(txtValue,"Not available")
                sentence = str(txtValue,"Not in my List or Google") 
                txtArea.insert(0.0,sentence)
            '''
   
    txtArea.insert(tk.END,dot_split)    
translator =  Translator() # Language Translator
master = tk.Tk()
master.geometry("470x370")
master.title("Tamil Language Definition App")

lbl = tk.Label(master,text='Enter the word to get synonym ')

nameEntered = tk.Entry(master,width=20) 
nameEntered.focus_set()

lbl.grid(row=0)
nameEntered.grid(row=0,column=1)

button = tk.Button(master, text = "Ok", command = callback, bg='blue',fg='white') 
button.grid(row=2,column=1,columnspan=2)

txtArea = tk.Text(master,width=35, height=13,wrap=tk.WORD)
txtArea.grid(row=3,column=1,columnspan=2,sticky=tk.W)
def txtEvent(event):
    if(event.state==12 and event.keysym=='c' ):
        return
    else:
        return "break"
txtArea.bind("<Key>", lambda e: txtEvent(e))

#time.sleep(8)
master.mainloop()
