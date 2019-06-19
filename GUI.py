from tkinter import *


# click function
def run_program():
    enteredText = textentry.get()  # collect data from text box entry
    if enteredText == "":
        textToDisplay = "Must enter text. Try again"
    # create another label
    else:
        textToDisplay = 'Email list downloaded ... check some folder'
    # clear label first
    Label(window, text="", bg='black',
          fg='white', font='none 12 bold').grid(row=2, column=0, sticky=W)
    Label(window, text=textToDisplay, bg='black',
          fg='white', font='none 12 bold').grid(row=2, column=0, sticky=W)


# define window
window = Tk()
window.title('Tournament Email Retrieve')
window.configure(background='black')

# add logo photos
photo = PhotoImage(file='Logo.gif')
photo2 = PhotoImage(file='JGHLogo.gif')
Label(window, image=photo, bg='Black').grid(row=0, column=0, sticky=W)
Label(window, image=photo2, bg='Black').grid(row=0, column=1, sticky=E)

# create label
Label(window, text='Enter tournament competitors URL', bg='black',
      fg='white', font='none 12 bold').grid(row=1, column=0, sticky=W)

# create text box entry for URL
textentry = Entry(window, width=50, bg='white')
textentry.grid(row=1, column=1, sticky=W)

# add a submit button
Button(window, text='Submit', width=7, command=run_program).grid(row=1, column=1, sticky=E)

# #  create a text box
# output = Text(window, width=55, height=6, wrap=WORD, background='White')
# output.grid(row=5, column=0, columnspan=2, sticky=W)

# display window
window.mainloop()
