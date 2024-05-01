from time import sleep
from celery import shared_task
from stadion.models import Club
import requests
from bs4 import BeautifulSoup


@shared_task()
def celery_task():
    print("start task")
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

        Club.objects.create(position=place.text, name=club.text, game=games.text,
                            score=score.text)

        print("salom")
        # # print("\n++++++\n", clubs, "\n++++++++\n")
        football_club.append(clubs.copy())
        # # print(football_club)
    print(football_club)

    sleep(10)  # Simulate expensive operation(s) that freeze Django
    print("end task +++ end task")
