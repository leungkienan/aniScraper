from bs4 import BeautifulSoup
import requests

episode_dict = {}
page_number = 0
animeTitle = "sword art online"
# need to grab data from a search query.
while True:
    page_number += 1
    url = "https://nyaa.si/user/Ember_Encodes?p=" + str(page_number)
    result = requests.get(url)
    if result.status_code != 200:
        break

    doc = BeautifulSoup(result.text, "html.parser")
    tableRows = doc.find_all('tr')

    for tr in tableRows:
        downloadTitle = tr.text.lower()
        if animeTitle in downloadTitle:
            a_tags = tr.find_all("a")
            for a in a_tags:
                dLink = a["href"]
                if "magnet" in dLink:
                    break
                if "view" in a["href"]:
                    epiNum = a.text
            episode_dict[epiNum] = dLink

print(dLink)
