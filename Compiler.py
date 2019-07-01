import EmailSearch
from MetPGAScrape import *
import xlrd
import os

# example athlete object list
x,y = met_pga_scrape("https://metpgajr.bluegolf.com/bluegolf/metpgajr16/event/metpgajr1613/contest/0/contestant/index.htm")


# function that takes list of athlete objects and the desired name of the output file
def email_list_get(ath_list, header="header", title="emails"):

    # name of the database file
    fileName = "AthleteProfileSheet.xlsx"

    # creates an empty list for putting in lists detailing names
    email_list = []
    not_found_list =[]

    # creates an xlrd workbook element and references the first sheet
    book = xlrd.open_workbook("AthleteProfileSheet.xlsx")
    sheet = book.sheet_by_index(0)

    # creates the search class and opens the found names and unfound names docs
    search = EmailSearch.SearchClass(fileName)
    name_found_doc = open(title + ".txt", "w+")
    not_found_doc = open(title + "notfound.txt", "w+")

    # for loop that runs through the athlete objects and runs a search on them, then adds their info
    # to a list
    for ath_obj in ath_list:
        id = search.performSearch(ath_obj.fname, ath_obj.lname, ath_obj.state, ath_obj.town)
        partial = search.get_partial()
        print(partial, ath_obj.fname, ath_obj.lname)
        if len(partial) != 0:
            print(ath_obj.fname, ath_obj.lname, ath_obj.state, ath_obj.town)
        # captures the athlete's name if not found but partially matched
        if len(id) == 0 and len(partial) != 0:
            text_rows = ath_obj.fname + "," + ath_obj.lname + "," + "partial match" + "," + "\n"
            not_found_list.append(text_rows)
        elif len(id) == 0:
            text_rows = ath_obj.fname + "," + ath_obj.lname + "," + "\n"
            not_found_list.append(text_rows)
        # captures the athlete's name if found
        for t in id:
            email = sheet.cell(t, 4).value
            # p_or_a = sheet.cell(t, 18).value <--- points towards athlete or parent attribute if needed
            text_rows = ath_obj.fname + "," + ath_obj.lname + "," + email + "," + "\n"
            email_list.append(text_rows)

    # converts list into dictionary into a list again to remove duplicates
    email_list = list(dict.fromkeys(email_list))
    not_found_list = list(dict.fromkeys(not_found_list))

    # runs through the email list and not found list and writes to files
    name_found_doc.write(header + '\n')
    not_found_doc.write(header + '\n')
    for row in email_list:
        name_found_doc.write(row)
    for row in not_found_list:
        not_found_doc.write(row)

    name_found_doc.close()
    not_found_doc.close()
    os.rename(title + ".txt", os.path.expanduser('~/Downloads/') + title + ".csv")
    os.rename(title + "notfound.txt", os.path.expanduser('~/Downloads/') + title + "notfound.csv")


email_list_get(x,y)