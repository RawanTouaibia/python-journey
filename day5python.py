import requests

API_KEY ="your_api_key_here"
try:
    city = input("enter city name: ")
    if not city.strip():
        print("please enter a city name")
    else:
    
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")

        data = response.json()
        if data["cod"] == "404":
            print("city not found")
        else:
            print(f"temperature: {data['main']['temp']}")
            print(f"weather description: {data['weather'][0]['description']}")
            print(f"humidity: {data['main']['humidity']}")
            print(f"wind speed: {data['wind']['speed']}")
except requests.exceptions.ConnectionError:
    print("no internet connection")