import xlrd
from bisect import bisect_left

class SearchClass:
    def __init__(self, data):
        # initialize variables
        self.dataFile = data
        self.workbook = xlrd.open_workbook(self.dataFile)
        self.sheet = self.workbook.sheet_by_index(0)
        self.lastnameList = []
        self.firstnameList = []
        self.searchedLastnameIndexList = []
        self.searchedFirstnameIndexList = []
        self.listOfID = []
        self.partial = []

    def binarySearch(self, a, x):
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return i
        else:
            return -1

    # gives back a list of indexes
    # where the last name mateches the searched last name
    def searchLastname(self, name):

        # get the column with all the last names
        for i in range(self.sheet.nrows):
            self.lastnameList.append(self.sheet.cell_value(i, 3).upper())
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
        # create list of all first names with that last name
        for j in self.searchedLastnameIndexList:
            self.firstnameList.append((self.sheet.cell_value(j, 2).upper()))

        firstNameIndex = self.firstnameList.index(nameF.upper())
        firstPlaceInSheet = self.searchedLastnameIndexList[firstNameIndex]
        k = firstPlaceInSheet
        # creates list of indecies in sheet where last + first name coincide
        while nameF.upper() == self.sheet.cell_value(k, 2).upper():
            self.searchedFirstnameIndexList.append(k)
            k += 1
        return self.searchedFirstnameIndexList

    # check if the indexes have corresponding: State, Torn
    def confirmStateTown(self, state, town):
        #open workbook
        for n in self.searchedFirstnameIndexList:
            if self.sheet.cell_value(n, 11).upper() != state.upper():
                self.searchedFirstnameIndexList.remove(n)
            elif self.sheet.cell_value(n, 10).upper() != town.upper():
                self.searchedFirstnameIndexList.remove(n)

    def getIds(self):
        allId = []
        for i in range(self.sheet.nrows):
            allId.append(self.sheet.cell_value(i,1))
        for k in self.searchedFirstnameIndexList:
            id = self.sheet.cell_value(k, 1)
            idIndex = allId.index(id)
            n = idIndex
            while self.sheet.cell_value(n, 1) == id:
                self.listOfID.append(n)
                n += 1



    # create over arching function that will run the whole program
    def performSearch(self, fname, lname, state, town):
        lasname = self.searchLastname(lname)
        if(len(lasname) >= 1):
            try:
                self.searchFirstname(fname)
                self.partial = self.searchedFirstnameIndexList
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

    def get_partial(self):
        partial_list = self.partial
        self.partial = []
        return partial_list
