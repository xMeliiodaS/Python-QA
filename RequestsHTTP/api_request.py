import requests


class ApiRequest:

    @staticmethod
    def get_all_houses():
        url = f"https://wizard-world-api.herokuapp.com/Houses"

        houses_respond = requests.get(url)

        print(houses_respond.status_code)
        print(houses_respond.json())
        return houses_respond.json()
