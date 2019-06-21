import requests
import lxml.html as lh
from Athlete import Athlete

# example site
site = "https://tournaments.hjgt.org/Tournament/TournamentDetails/0/Chicago-Summer-Junior-Open/11825"

def HJGT_scrape(url):

    ath_list =[]

    # pulls the HTML page
    page = requests.get(url)

    # creates an HTML element
    doc = lh.fromstring(page.content)

    # pulls in the title of the tournament
    title_raw = doc.get_element_by_id("pagecontainer")
    title_raw = title_raw.text_content().split('\n')
    title = title_raw[8]
    print(title)



    # finds all classes with the "tournamentparticipantbox" name
    participant_list = doc.find_class("tournamentparticipantbox")

    # runs through all of the paricipant containers
    for t in participant_list:
        ########## NAME ##########
        # takes out the raw tag elements containing player names
        name_raw = t.find_class("detailsparticipantname")
        # takes the raw name input and cleans up the odd tags and spaces
        fullname = name_raw[0].text_content()
        fullname = fullname.replace("\r", "")
        fullname = fullname.replace("\n", "")
        fullname = fullname.strip(" ")
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

        location_raw = t.find_class("detailsparticipantdisplayhometown")
        location = location_raw[0].text_content()
        location = location.replace("\r", "")
        location = location.replace("\n", "")
        location = location.strip(" ")
        location = location.split("Class of")[0]
        if "," in location:
            city = location.split(", ")[0]
            state = location.split(", ")[1].strip(" ")
        ath_list.append(Athlete(fname, lname, city, state))
    return ath_list, title


x = HJGT_scrape(site)

