# If we want to scrape a website, there are two ways
# 1. Use the API.
# 2. HTML web scraping using some tools like bs4

# Step 0: Installing the requirements(requests, html5lib, bs4) using pip command

import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# Step 1: Fetch the HTML

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2: Parse the HTML

soup = BeautifulSoup(htmlContent, 'html.parser') 
# print(soup.prettify())

# Step 3: HTML Tree Traversal

title = soup.title # Get the title of the HTML page.
print(title)

# Commonly used types of objects:
# 1. Tag  print(type(title))
# 2. NavigableString print(type(title.string))
# 3. BeautifulSoup print(type(soup))
# 4. Comment

# Get all the paragraphs from the page
paragraphs = soup.find_all('p')
print(paragraphs)

# Get first element of the given tag in the HTML page
print(soup.find('p'))

# Get the classes of the tag in the HTML page
print(soup.find('p')['class'])

# Find all the elements with a class names text-gray-500
print(soup.find_all('p', class_ = "text-gray-500"))

# Get the text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())

# Get all the anchors from the page
anchors = soup.find_all('a')
print(anchors)

all_links = set()
# Get all the links from anchor tags
for link in anchors:
    link_retrieved = link.get('href')
    if("https" not in link_retrieved):
        new_link = "https://codewithharry.com" + link_retrieved
        all_links.add(new_link)
    else:
        all_links.add(link_retrieved)

for i in all_links:
    print(i)
    
# Comment
tag1 = "<p><!--This is a comment--></p>"
soup2 = BeautifulSoup(tag1)
print(soup2.p)
print(soup2.p.string)
print(type(soup2.p.string))


flex = soup.find(class_ = "flex")

# .contents -> A tag's children are available as a list(Memory is used)
# .children -> A tag's children are available as generator(Memory is not used)

for i in flex.children:
    print(i)
    
for i in flex.contents:
    print(i)
    
for i in flex.strings:  # Gives the strings in tag where class name is flex 
    print(i)
    
print(flex.parent)

for i in flex.parents:
    print(i.name)
    
print(flex.next_sibling.next_sibling)
print(flex.previous_sibling)

elem_id = soup.select("#nav-content")
print(elem_id)

elem_class = soup.select(".flex")
print(elem_class)