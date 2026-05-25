#Q1) Study the open weather API show more data in your API calling program



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
    #c0310c3e6b093e54a1ad198ed7d07056
    api_key = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=#YOUR_API_KEY&units=metric"
    try:
        response = requests.get(api_key)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()

        
        print("Temperature: " + str(data['main']['temp']))
        print("Feels Like: " + str(data['main']['feels_like']))
        print("Minimum Temperature: " + str(data['main']['temp_min']))
        print("Maximum Temperature: " + str(data['main']['temp_max']))
        print("Pressure: " + str(data['main']['pressure']))
        print("Humidity: " + str(data['main']['humidity']))
        print("Sea Level: " + str(data['main']['sea_level']))
        print("Ground Level: " + str(data['main']['grnd_level']))
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

city_name = input("Enter the city name: ")
weather_api(city_name)
