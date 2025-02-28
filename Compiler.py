import EmailSearch
from MetPGAScrape import *
import xlrd
import os

# example athlete object list
x = met_pga_scrape("https://metpgajr.bluegolf.com/bluegolf/metpgajr16/event/metpgajr161/contest/0/contestant/index.htm")


# function that takes list of athlete objects and the desired name of the output file
def email_list_get(ath_list, header, title = "emails"):

    # name of the database file
    fileName = "AthleteProfileSheet.xlsx"

    # creates an empty list for putting in lists detailing names
    email_list = []

    # creates an xlrd workbook element and references the first sheet
    book = xlrd.open_workbook("AthleteProfileSheet.xlsx")
    sheet = book.sheet_by_index(0)

    search = EmailSearch.SearchClass(fileName)
    text_doc = open(title + ".txt", "w+")

    # for loop that runs through the athlete objects and runs a search on them, then adds their info
    # to a list
    for ath_obj in ath_list:
        id = search.performSearch(ath_obj.fname, ath_obj.lname, ath_obj.state, ath_obj.town)
        for t in id:
            email = sheet.cell(t, 4).value
            # p_or_a = sheet.cell(t, 18).value <--- points towards athlete or parent attribute if needed
            text_rows = ath_obj.fname + "," + ath_obj.lname + "," + email + "," + "\n"
            email_list.append(text_rows)

    # converts list into dictionary into a list again to remove duplicates
    email_list = list(dict.fromkeys(email_list))

    # runs through the email list and writes to file
    text_doc.write(header + '\n')
    for row in email_list:
        text_doc.write(row)

    text_doc.close()
    os.rename(title + ".txt", os.path.expanduser('~/Downloads/') + title + ".csv")