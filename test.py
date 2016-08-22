import requests
import re

def print_results(response, dict_key, number):
    for index, item in enumerate(response['results'], number):
        print(index, item[dict_key])

def call_api(data):
    number = 1
    url, dict_key, url_key = data
    response = requests.get(url).json()
    print_results(response, dict_key, number)
    number += 100
    if response['next']:
        while response['next']:
            more = input("* Do you want to see more? Y/n \n* or # of item to see details.\n").lower()
            if more == "y":
                url = response['next']
                response = requests.get(url).json()
                print_results(response, dict_key, number)
                number += 100
            elif more == "n":
                welcome()
            else:
                more = int(more)
                url = 'http://127.0.0.1:8000/api/{}/{}/'.format(url_key, more)
                response = requests.get(url).json()
                for key, value in response.items():
                    print('{}: {}'.format(key, value))
                welcome()

def welcome():
    choice = int(input('''
What do you want to see?
1: Movies
2: Raters
3: Rating
4: Exit
    '''))

    if choice == 4:
        exit()
    else:
        choice_dict = {
        1: ["http://127.0.0.1:8000/api/movies/", "movie_title", "movies"],
        2: ["http://127.0.0.1:8000/api/raters/", "age", "raters"],
        3: ["http://127.0.0.1:8000/api/ratings/", "rating", "ratings"],
        }
        call_api(choice_dict[choice])

welcome()
