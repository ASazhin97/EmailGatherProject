from tkinter import *
#from MetPGAScrape import met_pga_scrape

# click function
def button_clicked(textEntry, file_name_entry, window):
    URL = textEntry.get()  # collect data from text box entry
    file_name = file_name_entry.get()
    if URL == "" or file_name == "":
        textToDisplay = "Must enter text. Try again"
    # create another label
    else:
        textToDisplay = 'Email list downloaded ... check some folder'
    # clear label first
    Label(window, text=textToDisplay, bg='black',
          fg='white', font='none 12 bold').grid(row=3, column=0, sticky=W)

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

    # create label for URL entry
    labelText = 'Enter tournament competitors URL'
    Label(window, text=labelText, bg='black',
          fg='white', font='none 12 bold').grid(row=1, column=0, sticky=W)
    # create text box entry for URL
    URL_entry = Entry(window, width=50, bg='white')
    URL_entry.grid(row=1, column=1, sticky=W)

    # create label and text box for file name
    labelText2 = 'Enter name of document to output'
    Label(window, text=labelText2, bg='black',
          fg='white', font='none 12 bold').grid(row=2, column=0, sticky=W)
    file_name_entry = Entry(window, width=50, bg='white')
    file_name_entry.grid(row=2, column=1, sticky=W)


    # add a submit button for URL and file name

    Button(window, text='Submit', width=7, command=lambda: button_clicked(URL_entry, file_name_entry, window)).grid(
        row=2, column=1, sticky=E)

    # display window
    window.mainloop()

UI()