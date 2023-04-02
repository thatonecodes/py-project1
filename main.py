import requests
from bs4 import BeautifulSoup

# div class "C1_dkKeNHYB"
link = "https://www.kijiji.ca/b-entertainment/city-of-toronto/c165l1700273"
re = requests.get(link)
soup = BeautifulSoup(re.content, "html.parser")
results = soup.find(id="mainPageContent")
specificresults = soup.find("main")
printed_links = set()
# prints titles of ads
def find_and_print_listing():
    for resultats in results.find_all("div", class_="container-results large-images"):
        find_titles = resultats.find("a", class_="title")
        if find_titles is not None:
            print(find_titles.text.strip())
        get_desc = resultats.find("td", class_="description")
        if get_desc is not None:
            print(get_desc.text.strip())
        get_ad_link = find_titles.get("href")
        if get_ad_link is not None and get_ad_link not in printed_links:
            print(get_ad_link)

        printed_links.add(get_ad_link)

        print()
find_and_print_listing()