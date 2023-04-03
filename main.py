import requests
from bs4 import BeautifulSoup
import webbrowser
try:
    print("Please input your desired kijiji link: ")

    usrinput = input("Input: ")

    if "kijiji.ca" not in usrinput:
        print("Invalid Kijiji link!")
        quit()
except requests.exceptions.MissingSchema:
    print("Invalid URL!")
    

url = usrinput
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
# search main
ad_table = soup.find("main")
# search in main, div top feature
div_ad_elems = ad_table.find_all("div", class_="info")



def table_print(counter):
    for div_ad_elem in div_ad_elems:
        title = div_ad_elem.find("div", class_="title").text.strip()
        description = div_ad_elem.find("div", class_="description").text.strip()
        price = div_ad_elem.find("div", class_="price").text.strip()
        location = div_ad_elem.find("div", class_="location").text.strip()
        link = div_ad_elem.find("a", class_="title")["href"]
        print("Title: ", title)
        print("Description: ", description)
        print("Price: ", price)
        print("Link: ", "https://kijiji.ca" + link)
        print("Ad Number: ", counter)
        print("Location: ", location)
        counter = counter + 1
        print()
table_print(1)