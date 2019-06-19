import EmailSearch
from MetPGAScrape import *
import xlrd
import xlwt
from os.path import expanduser

# example athlete object list
x = met_pga_scrape("https://metpgajr.bluegolf.com/bluegolf/metpgajr16/event/metpgajr165/contest/0/contestant/index.htm")

def email_list_get(ath_list):

    # name of the database file
    fileName = "AthleteProfileSheet.xlsx"

    # creates an xlrd workbook element and references the first sheet
    book = xlrd.open_workbook("AthleteProfileSheet.xlsx")
    sheet = book.sheet_by_index(0)

    search = EmailSearch.SearchClass(fileName)
    for ath_obj in ath_list:
        id = search.performSearch(ath_obj.fname, ath_obj.lname, ath_obj.state, ath_obj.town)
        for t in id:
            email = sheet.cell(t, 4).value
            p_or_a = sheet.cell(t,18).value
            print("name:", ath_obj.fname, ath_obj.lname, "email", email, "p_or_a", p_or_a)




email_list_get(x)