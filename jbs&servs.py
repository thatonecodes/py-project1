import requests
from bs4 import BeautifulSoup
import webbrowser
print("Please input your desired kijiji link: *NO FRONT PAGE YET* PLEASE DO Services or Jobs TABS!")
usrinput = input("Input: ")
if "kijiji.ca" not in usrinput:
    print("Invalid Kijiji link!")
    quit()
url = usrinput

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')

# find all divs that contain the ads
ad_divs = soup.find_all('table')

for ad_div in ad_divs:
    # extract the title and description from each ad div
    title = ad_div.find('a', {'class': 'title'}).text.strip()
    description = ad_div.find('p').text.strip()
    kj_link = ad_div.find('a', {'class': 'title'})['href']
    print('Title:', title)
    print('Description:', description)
    clickable_link = f"\033[94m{kj_link}\033[0m"  # add color to the link
    print('Link: ', clickable_link)
    webbrowser.open(kj_link)
    print('---------------------')
#, {'class': 'description'}