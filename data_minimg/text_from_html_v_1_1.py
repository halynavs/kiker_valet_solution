from bs4 import BeautifulSoup
import numpy as np

# html tags with possible text
html_text_tag_list = ['p','li', 'h1', 'h2', 'h3', 'h4', 'h5',]


# find text in html and put it to single string
def find_text_to_string(source):
    if type(source) != str : return ""
    soup = BeautifulSoup(source, 'lxml')
    tags = soup.find_all(html_text_tag_list)
    text_contents = ""
    for tag in tags: 
        if tag.text != None:
            text_contents+=" " + tag.text.lower()
    return text_contents


# find text in html and put it to list
def find_text(source):
    if type(source) != str : return []
    soup = BeautifulSoup(source, 'lxml')
    tags = soup.find_all(html_text_tag_list)
    text_contents = []
    for tag in tags: 
        if tag.text != None:
            text_contents.append(tag.text.lower())
    return text_contents


# find text in list of htmls
def convert_list_of_html(source): 
    listed_source = np.empty(source.size, dtype=object)

    for i in range(source.size):
        listed_source[i] = find_text(source[i])

    return listed_source


def convert_list_of_html_to_string(source):
    listed_source = np.empty(source.size, dtype=object)

    for i in range(source.size):
        listed_source[i] = find_text_to_string(source[i])

    return listed_source