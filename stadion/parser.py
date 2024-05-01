from stadion.models import Club
import requests
from bs4 import BeautifulSoup

result = requests.get("https://stadion.uz/").text

doc = BeautifulSoup(result, "html.parser")

table_of_places = doc.select("#standings_place")[0]

football_club = []
clubs = {}

tdses = table_of_places.find_all("tr")[1:21]
x = 1
for tds in tdses:
    place = tds.find_all("td")[0]
    club = tds.find_all("td")[2]
    games = tds.find_all("td")[3]
    score = tds.find_all("td")[4]
    clubs["place"] = place.text
    clubs["club"] = club.text
    clubs["games"] = games.text
    clubs["score"] = score.text


    # # print("\n++++++\n", clubs, "\n++++++++\n")
    football_club.append(clubs.copy())
    # # print(football_club)
print(football_club)

# Club.objects.create(place=football_club[0]["place"], name=football_club[0]["club"], game=football_club[0]["game"],
#                     score=football_club[0]["score"])
# Club.save()
