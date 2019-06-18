import requests
import lxml.html as lh
import pandas as pd

url='https://metpgajr.bluegolf.com/bluegolf/metpgajr19/event/metpgajr195/contest/0/contestant/index.htm'

#Create a handle, page, to handle the contents of the website
page = requests.get(url)

#Store the contents of the website under doc
doc = lh.fromstring(page.content)

#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')

#Create empty list
col=[]
i=0

######Name Extraction##########
for t in tr_elements[1:]:

    cell_content = t.text_content()
    fullname = cell_content.split("\n")[2]
    fname = fullname.split(" ")[0]
    lname = fullname.split(" ")[1]

#def met_pga_scrape
# for t in tr_elements[1:]:
#
#     cell_content = t.text_content()
#     fullname = cell_content.split("\n")[2]
#     fname = fullname.split(" ")[0]
#     lname = fullname.split(" ")[1]

