#Q3) Search for more free API's generate your and call them to fetch data. Display some data in your program.

#jokes api
import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()
        print("Joke:", joke["setup"])
        print(" punchline:", joke["punchline"])
    else:
        print("Failed to fetch joke")

get_joke()