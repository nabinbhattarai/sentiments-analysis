from tkinter import *
import tkinter
from textblob import TextBlob
from tkinter import filedialog


root = tkinter.Tk()
root.title("Sentiments analysis")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0,0)

def submit():
    text = text_var.get()
    blob = TextBlob(text)
    
    labelResult = Label(
        root,
        font = ("Times",20, "bold")
        )
    labelResult.pack(pady=(150,5))
    
    if blob.sentiment.polarity > 0:
        labelResult.configure(text="The text provided is positive")
    elif(blob.sentiment.polarity<0):
        labelResult.configure(text="The text provided is negative")
    else:
        labelResult.configure(text="The text provided is neutral")


#browsing the file from local storage  
def browse():
    text_file= filedialog.askopenfilename(initialdir="C:/Administrator/Desktop/", filetypes=(("txt files","*.txt"),("allfiles","*.*")))
    welcomeNote.destroy()
    text_label.destroy()
    text_entry.destroy()
    submitButton.destroy()
    choose_file.destroy()
    browseButton.destroy()

    positiveResult = Label(
        root,
        font = ("Times",15, "bold"),
        bg = "#ffffff"
        )
    positiveResult.pack(pady=(50,20))

    negativeResult = Label(
        root,
        font = ("Times",15, "bold"),
        bg = "#ffffff"
        )
    negativeResult.pack(pady=(20,50))

    neutralResult = Label(
        root,
        font = ("Times",15, "bold"),
        bg = "#ffffff"
        )
    neutralResult.pack(pady=(5,50))
   
    pos_sample = 0
    pos_lines = 0
    neg_sample = 0
    neg_lines = 0
    neu_lines = 0
    neu_sample = 0
    
    text_file = open(text_file,'r')
    stuff = text_file.read()
    for line in stuff.split('\n'): 
        analysis = TextBlob(line)
        if analysis.sentiment.polarity > 0: #if polarity is greater than 0, it is positive text
            pos_lines += 1
        pos_sample +=1
        
        if analysis.sentiment.polarity < 0:
            neg_lines += 1
        neg_sample +=1

        if analysis.sentiment.polarity == 0:
            neu_lines += 1
        neu_sample +=1
        
    #calculating positive,negative and neutral sentiments percentage
    negativeResult.configure(text="Negative sentiments percentage = {}% via {} samples \n where negative lines are : {}".format((neg_lines/neg_sample)*100.0, neg_sample,neg_lines))
    positiveResult.configure(text="Positive sentiments percentage = {}% via {} samples \n where positive lines are : {}".format((pos_lines/pos_sample)*100.0, pos_sample,pos_lines))
    neutralResult.configure(text="Neutral sentiments percentage = {}% via {} samples \n where neutral lines are : {}".format((neu_lines/neu_sample)*100.0, neu_sample,neu_lines))

welcomeNote = Label(
    root,
    text= "Welcome to the sentiments analysis",
    font= ("Times",22,"bold"),
    fg = "#ff3300",
    bg = "#ffffff" 
    )
welcomeNote.pack(pady=(50,50))

text_var = tkinter.StringVar()


text_label = tkinter.Label(root,
             text="Enter the text:",
             bg = "#ffffff" ,
             font=("Times",15,'bold')
             )



text_entry = tkinter.Entry(root,
                   textvariable= text_var,
                   font=('calibre',10),
                   bg ="#00ccff",
                   fg = "#000000",
                   width = 45,
                   )
submitButton=Button(root,
                    text="Submit",
                    command = submit
                    )
choose_file = Label(
    root,
    text="Browse the file to be analyzed(only .txt files)",
    font=("Times",12,"bold"),
    bg = "#ffffff"
    )

browseButton = Button(root,
                    text="Browse",
                    font = ("Times",12,"bold"),
                    command = browse
                    )



text_label.pack()
text_entry.pack()
submitButton.pack(pady=(5,50))
choose_file.pack()
browseButton.pack()

root.mainloop()   
