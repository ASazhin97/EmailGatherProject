import xlrd
from bisect import bisect_left

class SearchClass:
    def __init__(self, data):
        # initialize variables
        self.dataFile = data
        self.lastnameList = []
        self.firstnameList = []
        self.searchedLastnameIndexList = []
        self.searchedFirstnameIndexList = []
        self.listOfID = []

    def binarySearch(self, a, x):
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return i
        else:
            return -1

    # gives back a list of indexes
    # where the last name mateches the searched last name
    def searchLastname(self, name):
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
        return self.searchedLastnameIndexList

    # using the previously found list of indexes of lastnames
    # find in those the lis of indexes where the name matches
    def searchFirstname(self, nameF):
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
    def confirmStateTown(self, state, town):
        #open workbook
        workbook = xlrd.open_workbook(self.dataFile)
        sheet = workbook.sheet_by_index(0)
        for n in self.searchedFirstnameIndexList:
            if sheet.cell_value(n, 11).upper() != state.upper():
                self.searchedFirstnameIndexList.remove(n)
            elif sheet.cell_value(n, 10).upper() != town.upper():
                self.searchedFirstnameIndexList.remove(n)

    def getIds(self):
        workbook = xlrd.open_workbook(self.dataFile)
        sheet = workbook.sheet_by_index(0)
        allId = []
        for i in range(sheet.nrows):
            allId.append(sheet.cell_value(i,1))
        for k in self.searchedFirstnameIndexList:
            id = sheet.cell_value(k, 1)
            idIndex = allId.index(id)
            n = idIndex
            while sheet.cell_value(n, 1) == id:
                self.listOfID.append(n)
                n += 1



    # create over arching function that will run the whole program
    def performSearch(self, fname, lname, state, town):
        lasname = self.searchLastname(lname)
        if(len(lasname) >= 1):
            try:
                self.searchFirstname(fname)
                self.confirmStateTown(state, town)
                self.getIds()
            except:
                print("not in list")

        returnlist = self.listOfID
        self.lastnameList = []
        self.firstnameList = []
        self.searchedLastnameIndexList = []
        self.searchedFirstnameIndexList = []
        self.listOfID = []
        return returnlist


