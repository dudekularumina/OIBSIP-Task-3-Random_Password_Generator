from tkinter import *
from random import randint

root=Tk()
root.title("Strong Password Generator")
root.iconbitmap("")
root.geometry("500x500")


def new_rand():
    #clear entry box
    pw_entry.delete(0, END)

    #get password length and convert into int
    pw_length=int(my_entry.get())

    #create a variable to hold our password
    my_password=''

    # Loop through password length
    for x in range(pw_length):
        my_password+=chr(randint(33, 126))

    # Output password to th escreen
    pw_entry.insert(0, my_password)

#Label
lf=LabelFrame(root, text="How Many Characters?", font="sans 10 bold")
lf.pack(pady=20)

# Create Entry box to designate no.or Character
my_entry=Entry(lf, font=("Helvetica", 24))    
my_entry.pack(pady=20, padx=20)

# Create entry box for our Returned Password
pw_entry=Entry(root, text='', font=("Helvetica", 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

# Create a frame for our buttons
my_frame=Frame(root)
my_frame.pack(pady=20)

#create our buttons
my_button=Button(my_frame, text="Generate Strong Password", font="sans 16 bold", command=new_rand)
my_button.grid(row=0, column=0, padx=10)


root.mainloop()



