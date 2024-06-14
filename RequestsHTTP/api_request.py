import requests


class Requesta:

    def get_all_houses(self):
        url = f"https://wizard-world-api.herokuapp.com/Houses"

        houses_respond = requests.get(url)

        print(houses_respond.status_code)
        print(houses_respond.json())
        return houses_respond.json()
