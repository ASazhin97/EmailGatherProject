import requests
import lxml.html as lh
from Athlete import Athlete

site = 'https://metpgajr.bluegolf.com/bluegolf/metpgajr19/event/metpgajr195/contest/0/contestant/index.htm'

# function that passes in tournament roster URL and returns list of athlete objects
def met_pga_scrape(url):

    # Create a handle, page, to handle the contents of the website
    page = requests.get(url)

    # Store the contents of the website under doc
    doc = lh.fromstring(page.content)

    # Parse data that are stored between <tr>..</tr> of HTML
    tr_elements = doc.xpath('//tr')

    # Create's list of athlete objects
    ath_list = []


    for t in tr_elements[1:]:
        cell_content = t.text_content()
    ########### NAME ###########
        # extracts name from table by splitting it up from \n characters
        fullname = cell_content.split("\n")[2]
        # name is read-in in full, then split by spaces
        name_list = fullname.split(" ")
        # general name catch, will be used for basic first name and last name
        if len(name_list) == 2:
            fname = name_list[0]
            lname = name_list[1]
        # catches odd names such as "James Ryan III" or "M. William Geraldson"
        elif len(name_list) > 2:
            # Removes odd elements left by random spaces
            if "" in name_list:
                name_list.remove("")
            # catches names with periods like James. A or M.Gregory
            if name_list[0][-1] or name_list[1][-1] == ".":
                fname = name_list[0] + " " + name_list[1]
                lname = name_list[2]
            # Catches people with "II" or "III" endings
            elif name_list[-1][-1] == "I":
                fname = name_list[0]
                lname = name_list[1] + name_list[2]
            # generic catchall that will be updated as errors occur
            else:
                fname = name_list[0]
                lname = name_list[-1]

    ############# LOCATION #############
        # takes the full name string from the site
        location = cell_content.split("\n")[5]
        # checks if the location is in city, state template
        if "," in location:
            city = (location.split(", ")[0])
            state = (location.split(", ")[1])
        # checks if the location is in the city - state template
        elif "-" in location:
            city = location.split("-")[0]
            if city[-1] == " ":
                city = city[:-1]
            state = location.split("-")[-1].strip(" ")
        ath_list.append(Athlete(fname, lname, city, state))
    return ath_list

print(met_pga_scrape(site))