from random import choice
import requests

def fetch_fact():
    api_url = 'https://api.api-ninjas.com/v1/facts'
    response = requests.get(api_url, headers={'X-Api-Key': 'OunaPrs6VTPlzAPwYtqOzQ==GK2iGERCC61alMh6'})
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['fact']
        else:
            return "No facts were found."
    else:
        return f"Error: unable to fetch a fact. Status code {response.status_code}"
    
def fetch_weather(city_name):
    api_key = 'c4zmWjxrILFRN50mkGeSIQ71MPJhJjuq'
    url = f'https://api.tomorrow.io/v4/weather/forecast?location={city_name}&apikey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        info = data["timelines"]['hourly'][0]
        temp = info['values']['temperature']
        uv = info['values']['uvIndex']
        return f"{city_name} has a temperature of {temp} degrees Celsius and a UV index of {uv}."
    else:
        return f'Error: unable to get weather forecast. Status code {response.status_code}'
    
def fetch_quote():
    url = 'https://zenquotes.io/api/random'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        json = data[0]
        quote = json['q']
        author = json['a']
        return f"{quote} - {author}"
    else:
        return f'Error: unable to get inspirational quote. Status code {response.status_code}'

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    split_params = lowered.split()
    if lowered == '':
        return 'Well, you are quiet.'
    elif 'hello' in lowered:
        return 'Hello there! Please let me know what you want me to do!'
    elif 'help' in lowered:
        return f'You can say !weather, !fact, or !quote.'
    elif '!fact' in lowered:
        print(fetch_fact)
    elif split_params[0] == "!weather":
        if len(split_params) > 1:
            city_name = ' '.join(split_params[1:])
            return fetch_weather(city_name)
        else:
            return 'Please provide a city name after the !weather command.'
    elif '!quote' in lowered:
        print(fetch_quote)
    else:
        return choice(['I don\'t have any brains.',
                       'What?',
                       "Repeat please."])