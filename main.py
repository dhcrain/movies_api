import requests
import re

def print_results(response, dict_key, number):
    for index, item in enumerate(response['results'], number):
        print(index, item[dict_key])

def call_api(data):
    number = 1
    url, dict_key = data
    response = requests.get(url).json()
    print_results(response, dict_key, number)
    number += 100
    if response['next']:
        while response['next']:
            more = input("Do you want to see more? Y/n \n").lower()
            if more != "n":
                url = response['next']
                response = requests.get(url).json()
                print_results(response, dict_key, number)
                number += 100
            else:
                exit()

choice = int(input('''
What do you want to see?
1: Movies
2: Raters
3: Rating
'''))

choice_dict = {
1: ["http://127.0.0.1:8000/api/movies/", "movie_title"],
2: ["http://127.0.0.1:8000/api/raters/", "age"],
3: ["http://127.0.0.1:8000/api/ratings/", "rating"],
}
call_api(choice_dict[choice])
