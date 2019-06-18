import xlrd
from bisect import bisect_left

fileName = "AthleteProfileSheet.xlsx"
name = "Adelman"
nameF = "Ashley"


class SearchClass:
    def __init__(self, data):
        # initialize variables
        self.dataFile = data
        self.lastnameList = []
        self.firstnameList = []
        self.searchedLastnameIndexList = []
        self.searchedFirstnameIndexList = []

    def binarySearch(self, a, x):
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return i
        else:
            return -1

    # gives back a list of indexes
    # where the last name mateches the searched last name
    def searchLastname(self):
        #open book
        workbook = xlrd.open_workbook(self.dataFile)
        sheet = workbook.sheet_by_index(0)

        # get the column with all the last names
        for i in range(sheet.nrows):
            self.lastnameList.append(sheet.cell_value(i, 3).upper())
        # use binary search to find the first name
        firstIndex = self.binarySearch(self.lastnameList, name.upper())
        i = firstIndex
        # get the list of index for each last name
        while name.upper() == self.lastnameList[i]:
            self.searchedLastnameIndexList.append(i)
            i += 1

    # using the previously found list of indexes of lastnames
    # find in those the lis of indexes where the name matches
    def searchFirstname(self):
        #open workbook
        workbook = xlrd.open_workbook(self.dataFile)
        sheet = workbook.sheet_by_index(0)
        # create list of all first names with that last name
        for j in self.searchedLastnameIndexList:
            self.firstnameList.append((sheet.cell_value(j, 2).upper()))

        firstNameIndex = self.firstnameList.index(nameF.upper())
        firstPlaceInSheet = self.searchedLastnameIndexList[firstNameIndex]
        k = firstPlaceInSheet
        # creates list of indecies in sheet where last + first name coincide
        while nameF.upper() == sheet.cell_value(k, 2).upper():
            self.searchedFirstnameIndexList.append(k)
            k += 1

    # TO DO
    # check if the indexes have corresponding: State, Torn
    # if not correct throw out
    # if correct keep
    # get athlete profile id
    # get all indexes with that id
    # create overarching function that will run the searches
    # THIS FUNCTION SHOULD CLEAR ALL FIELD ONCE FINISHED
    # re-arragne to make standalone class

searchObject = SearchClass(fileName)
searchObject.searchLastname()
searchObject.searchFirstname()
print(searchObject.searchedFirstnameIndexList)