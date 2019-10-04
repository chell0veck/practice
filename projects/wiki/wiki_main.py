# import wikipedia
#
# print(wikipedia.page("List of Nobel laureates in Literature").html())

import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')

page_py = wiki_wiki.page('List_of_Nobel_laureates_in_Literature')

# print(page_py.sections)
print(page_py.section_by_title('Laureates'))

# push...