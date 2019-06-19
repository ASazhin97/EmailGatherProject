from tkinter import *
from MetPGAScrape import met_pga_scrape

# click function
def button_clicked(textEntry, window):
    url = textEntry.get()  # collect data from text box entry
    if url == "":
        textToDisplay = "Must enter text. Try again"
    # create another label
    else:
        ath_obj_list = met_pga_scrape(url)

        textToDisplay = 'Email list downloaded ... check some folder'
    # clear label first
    Label(window, text=textToDisplay, bg='black',
          fg='white', font='none 12 bold').grid(row=2, column=0, sticky=W)

def UI():
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
    labelText = 'Enter tournament competitors URL'
    Label(window, text=labelText, bg='black',
          fg='white', font='none 12 bold').grid(row=1, column=0, sticky=W)

    # create text box entry for URL
    textEntry = Entry(window, width=50, bg='white')
    textEntry.grid(row=1, column=1, sticky=W)

    # add a submit button

    b = Button(window, text='Submit', width=7, command=lambda: button_clicked(textEntry, window)).grid(
        row=1, column=1, sticky=E)

    # display window
    window.mainloop()
