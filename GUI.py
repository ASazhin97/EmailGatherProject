from tkinter import *


# click function
def click():
    enteredText = textentry.get()  # collect data from text box entry
    # print(enteredText)


# define window
window = Tk()
window.title('Tournament Email Retrieve')
window.configure(background='black')

# add photos
photo = PhotoImage(file='Logo.gif')
photo2 = PhotoImage(file='JGHLogo.gif')
Label(window, image=photo, bg='Black').grid(row=0, column=0, sticky=W)
Label(window, image=photo2, bg='Black', width=330).grid(row=0, column=1, sticky=W)

# create label
Label(window, text='Enter tour name', bg='gray',
      fg='white', font='none 12 bold').grid(row=1, column=0, sticky=W)

# create text box entry
textentry = Entry(window, width=20, bg='white')
textentry.grid(row=1, column=1, sticky=W)

# add a button
Button(window, text='Submit', width=7, command=click).grid(row=1, column=2, sticky=W)

# create another label
Label(window, text='Enter tournament URL', bg='black',
      fg='white', font='none 12 bold').grid(row=2, column=0, sticky=W)

#  create a text box
output = Text(window, width=75, height=6, wrap=WORD, background='White')
output.grid(row=5, column=0, columnspan=2, sticky=W)

# display window
window.mainloop()
