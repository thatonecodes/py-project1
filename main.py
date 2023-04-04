import requests
from bs4 import BeautifulSoup
try:
    print("Please input your desired kijiji link: ")

    usrinput = input("Input: ")

    if "kijiji.ca" not in usrinput:
        print("Invalid Kijiji link!")
        quit()
except requests.RequestException:
    print("Request exepection code " + requests.RequestException)
    
try:
    url = usrinput
    page = requests.get(url)
except requests.exceptions.MissingSchema:
        print("\n")
        print("Invalid link, no http or https found.")
        quit()

soup = BeautifulSoup(page.content, "html.parser")
# search main
ad_table = soup.find("main")
# search in main, div top feature
try:
    div_ad_elems = ad_table.find_all("div", class_="info")
except AttributeError:
        print("\n")
        print("Invalid link, unable to parse...(div not found).")
        quit()

def table_print(counter):
    try:
        for div_ad_elem in div_ad_elems:
            title = div_ad_elem.find("div", class_="title").text.strip()
            description = div_ad_elem.find("div", class_="description").text.strip()
            price = div_ad_elem.find("div", class_="price").text.strip()
            location = div_ad_elem.find("div", class_="location").text.strip()
            link = div_ad_elem.find("a", class_="title")["href"]
            print("\n")
            print("Title: ", title)
            print("Description: ", description)
            print("Price: ", price)
            print("Link: ", "https://kijiji.ca" + link)
            print("Ad Number: ", counter)
            print("Location: ", location)
            counter = counter + 1
            print()
    except NameError:
        print("\n")
        print("Sorry, Div Not Found in one of the defined Elements...")
        quit()

table_print(1)


