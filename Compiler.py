import EmailSearch

#name of the databse file
fileName = "AthleteProfileSheet.xlsx"


#these are just trial names
name = "Adelman"
nameF = "Ash"
state = "GA"
town = "Alpharetta"


search = EmailSearch.SearchClass(fileName)
ids = search.performSearch(nameF, name, state, town)
print(ids)

#for each id index, get email and if that email is parent or athlete
#put into text file