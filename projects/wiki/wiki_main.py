from urllib import request
from bs4 import BeautifulSoup
import wikipediaapi


# init data
lite = 'https://en.wikipedia.org/wiki/List_of_Nobel_laureates_in_Literature#Laureates'
page = request.urlopen(lite)
soup = BeautifulSoup(page, 'html.parser')
table = soup.find('table').find('tbody')
data = []

# build skeleton
for row in table.findAll('tr')[1:]:
    record = [ele.text.strip() for ele in row.findAll('td') if ele.text.strip()]
    data.append(record)

# add missing years
for idx, rec in enumerate(data):
    if not rec[0].isdigit():
        rec.insert(0, data[idx - 1][0])

# write to a file
# with open('lit', 'w') as file:
#     for record in data:
#         file.write('  '.join(record))
#         file.write('\n')


w = wikipediaapi.Wikipedia('en')

for rec in data:

    if len(rec) > 2:
        name = rec[1]

    print(w.page(name).sections)


