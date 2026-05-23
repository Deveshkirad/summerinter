import requests
""""temp": 308.77,
    "feels_like": 309.22,
    "temp_min": 308.77,
    "temp_max": 308.77,
    "pressure": 1007,
    "humidity": 32,
    "sea_level": 1007,
    "grnd_level": 960"""
def weather_api(city):
    api_key = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=#YOUR_API_KEY&units=metric"
    try:
        response = requests.get(api_key)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()

        
        print(data['main']['temp'])
        print(data['main']['feels_like'])
        print(data['main']['temp_min'])
        print(data['main']['temp_max'])
        print(data['main']['pressure'])
        print(data['main']['humidity'])
        print(data['main']['sea_level'])
        print(data['main']['grnd_level'])
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

city_name = input("Enter the city name: ")
weather_api(city_name)
