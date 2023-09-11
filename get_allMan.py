import requests
from bs4 import BeautifulSoup
import json
import re

url = ""

def find_All(soup, tagType , tagClassName=""):
    if tagClassName != "":
        item_all = soup.find_all( tagType , class_= tagClassName)
    else :
        item_all = soup.find_all( tagType)
    return item_all

def find_One(soup, tagType , tagClassName=""):
    if tagClassName != "":
        item = soup.find( tagType , class_= tagClassName)
    else :
        item = soup.find( tagType)
    return item


def get_page_home_items(id):
    # Construct the link with the given id
    link = url + "page/{}".format(id)
    print(link)

    # Make a GET request to the link
    response = requests.get(link)

    # Create a BeautifulSoup object with the response text and parse it with HTML parser
    soup = BeautifulSoup(response.text, "html.parser", from_encoding="utf-8")

    # Find all elements with "div" tag and class "page-item-detail"
    item_all = find_All(soup, "div" , "page-item-detail")

    # Initialize an empty list to store all items
    list_all_item = []

    # Loop through each item
    for item in item_all:
        # Initialize a dictionary to store item details
        item_detali = {
            "item_name": '',
            "item_img": '',
            "item_list_chp1": '',
            "item_list_chp2": '',
            "item_list_chp1_dIm": '',
            "item_list_chp2_dIm": ''
        }

        # Find all elements with "img" tag and store their "src" values in a list
        src_list = []
        img_all = find_All(item, "img")
        for img in img_all:
            src = img.get("src")
            src_list.append(src)

        # Find all elements with "span" tag and class "post-on" and store their text values in a list
        text_list = []
        span_all = find_All(item, "span" , "post-on")
        for span in span_all:
            text = span.text
            text_list.append(text)

        # Filter the text list to only include values with digits
        text_list = [s for s in text_list if  re.search('[0-9]', s)]
        # Flatten the nested list and filter to only include values with digits
        text_list = [ [j for j in i if  re.search('[0-9]', j)] 
                      for i in [i.split("\t") for i in text_list] ]

        # Check the length of src_list and populate the item_detali dictionary accordingly
        if len(src_list) > 2:
            item_detali["item_img"] = src_list[0]
            item_detali["item_list_chp1_dIm"] = src_list[1]
            item_detali["item_list_chp2_dIm"] = src_list[2]
        elif len(src_list) == 2 :
            item_detali["item_img"] = src_list[0]
            item_detali["item_list_chp1_dIm"] = src_list[1]
            if len(text_list) > 0 :
                item_detali["item_list_chp2_dIm"] = text_list[0]
        elif len(src_list) < 2 :
            item_detali["item_img"] = src_list[0]
            if len(text_list) > 0 :
                item_detali["item_list_chp1_dIm"] = text_list[0]
                if len(text_list) > 1 :
                    item_detali["item_list_chp2_dIm"] = text_list[1]

        # Initialize a list to store the text content of the "a" elements
        a_list = []
        # Find all "a" elements in the item and store their text content in the a_list
        a_all = find_All(item, "a")
        for a in a_all:
            text = a.text
            a_list.append(text)

        # Store the second element of the a_list in the item_detali dictionary as item_name
        item_detali["item_name"] = a_list[1]
        item_detali["item_path_name"] =a_all[1].get("href").split("/")[-2]

        # Find all elements in the a_list that contain a number
        list_chp = [s for s in a_list if  re.search('[0-9]', s)]
        # If there are at least one such elements, store the first and second elements in item_detali dictionary as item_list_chp1 and item_list_chp2, respectively
        if len(list_chp) >= 1:
            item_detali["item_list_chp1"] = list_chp[0]
            if len(list_chp) == 2:
                item_detali["item_list_chp2"] = list_chp[1]
        # If there are no such elements, store empty strings in item_list_chp1 and item_list_chp2
        else :
            item_detali["item_list_chp1"] = ''
            item_detali["item_list_chp2"] = ''
        # Append the item_detali dictionary to the list_all_item list
        list_all_item.append(item_detali)

    # Return the list_all_item list
    return list_all_item

def get_page_category_items(catey,id):
    link = url + "manga-genre/{}/page/{}".format(catey , id)
    print(link)
    # Make a GET request to the link
    response = requests.get(link)

    # Create a BeautifulSoup object with the response text and parse it with HTML parser
    soup = BeautifulSoup(response.text, "html.parser", from_encoding="utf-8")

    # Find all elements with "div" tag and class "page-item-detail"
    item_all = find_All(soup, "div" , "page-item-detail")

    # Initialize an empty list to store all items
    list_all_item = []

    # Loop through each item
    for item in item_all:
        # Initialize a dictionary to store item details
        item_detali = {
            "item_name": '',
            "item_img": '',
            "item_list_chp1": '',
            "item_list_chp2": '',
            "item_list_chp1_dIm": '',
            "item_list_chp2_dIm": ''
        }

        # Find all elements with "img" tag and store their "src" values in a list
        src_list = []
        img_all = find_All(item, "img")
        for img in img_all:
            src = img.get("src")
            src_list.append(src)

        # Find all elements with "span" tag and class "post-on" and store their text values in a list
        text_list = []
        span_all = find_All(item, "span" , "post-on")
        for span in span_all:
            text = span.text
            text_list.append(text)

        # Filter the text list to only include values with digits
        text_list = [s for s in text_list if  re.search('[0-9]', s)]
        # Flatten the nested list and filter to only include values with digits
        text_list = [ [j for j in i if  re.search('[0-9]', j)] 
                      for i in [i.split("\t") for i in text_list] ]

        # Check the length of src_list and populate the item_detali dictionary accordingly
        if len(src_list) > 2:
            item_detali["item_img"] = src_list[0]
            item_detali["item_list_chp1_dIm"] = src_list[1]
            item_detali["item_list_chp2_dIm"] = src_list[2]
        elif len(src_list) == 2 :
            item_detali["item_img"] = src_list[0]
            item_detali["item_list_chp1_dIm"] = src_list[1]
            if len(text_list) > 0 :
                item_detali["item_list_chp2_dIm"] = text_list[0]
        elif len(src_list) < 2 :
            item_detali["item_img"] = src_list[0]
            if len(text_list) > 0 :
                item_detali["item_list_chp1_dIm"] = text_list[0]
                if len(text_list) > 1 :
                    item_detali["item_list_chp2_dIm"] = text_list[1]

        # Initialize a list to store the text content of the "a" elements
        a_list = []
        # Find all "a" elements in the item and store their text content in the a_list
        a_all = find_All(item, "a")
        for a in a_all:
            text = a.text
            a_list.append(text)

        # Store the second element of the a_list in the item_detali dictionary as item_name
        item_detali["item_name"] = a_list[1]
        item_detali["item_path_name"] =a_all[1].get("href").split("/")[-2]

        # Find all elements in the a_list that contain a number
        list_chp = [s for s in a_list if  re.search('[0-9]', s)]
        # If there are at least one such elements, store the first and second elements in item_detali dictionary as item_list_chp1 and item_list_chp2, respectively
        if len(list_chp) >= 1:
            item_detali["item_list_chp1"] = list_chp[0]
            if len(list_chp) == 2:
                item_detali["item_list_chp2"] = list_chp[1]
        # If there are no such elements, store empty strings in item_list_chp1 and item_list_chp2
        else :
            item_detali["item_list_chp1"] = ''
            item_detali["item_list_chp2"] = ''
        # Append the item_detali dictionary to the list_all_item list
        list_all_item.append(item_detali)

    # Return the list_all_item list
    return list_all_item

def get_page_single_item(name):
    link = url + "manga/{}".format(name)
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser", from_encoding="utf-8")
    item_detali = {}

    # Scraping Detali of Manhwa
    title = find_One(soup, "div" , "post-title")
    title_text = find_One(title, "h1").text
    title_text = [s for s in title_text.split("  ") if  re.search('[a-z]', s)][0].split("\t")[-1]
    tab_summary  = find_One(soup, "div" , "tab-summary")
    summary_image  = find_One(tab_summary, "div" , "summary_image")

    image  = find_One(summary_image, "img").get("src")
    total_votes = find_One(tab_summary, "span" , "total_votes").text
    summary_content = find_All(tab_summary, "div" , "summary-content")
    author_content = find_One(tab_summary, "div" , "author-content").text
    artist_content = find_One(tab_summary, "div" , "artist-content").text
    genres_content = find_One(tab_summary, "div" , "genres-content").text
    item_detali["item_name"]= title_text
    item_detali["item_img"]= image
    item_detali["total_votes"]= total_votes
    item_detali["author_content"]= author_content
    item_detali["artist_content"]= artist_content
    item_detali["other_names"]= summary_content[1].text
    item_detali["item_type"]= summary_content[5].text
    item_detali["genres_content"]= genres_content.split(",")

    # Scraping Story
    item_story = {}
    description_summary = find_One(soup, "div" , "description-summary").text
    item_story["description"] = description_summary 

    # Scraping All Chapter
    item_chapters = []
    listing_chapters_wrap = find_One(soup, "div" , "listing-chapters_wrap")
    all_chapter = find_All(listing_chapters_wrap , "li" , "wp-manga-chapter")
    for chap in all_chapter :
        chapter = {}
        all_a = find_All(chap, "a")
        chapter["chap_Numbre"] = [s for s in all_a[0].text.split("\t") if  re.search('[0-9]', s)][0]
        if len(all_a) > 1 :
            chapter["chap_img"] = find_One(all_a[1], "img").get("src")
            chapter["chap_date"] = ""
        else :
            chapter["chap_img"] = ""
            chapter["chap_date"] = find_One(chap, "i").text
        item_chapters.append(chapter)
    
    data = {"item_detali" : item_detali , "item_story" : item_story , "item_chapters" : item_chapters }

    return data

def get_page_single_chapter(name , chapter):
    link = url + "manga/{}/{}".format(name,chapter)
    print( "Link : --- " + link)
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser", from_encoding="utf-8")
    chapter_imges = []

    # Scraping Detali of Manhwa
    reading_content = find_One(soup, "div" , "reading-content")
    print(reading_content)
    all_Images = find_All(reading_content, "img")
    for i in range(len(all_Images)):
        img = all_Images[i].get("src")
        chapter_imges.append( { i : img.split("\t")[-1]})
    return { "chapter_imges" : chapter_imges}

def p():
    return {"nou" : "ddd"}
