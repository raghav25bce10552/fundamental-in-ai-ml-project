import requests

cities = {
    "bhopal": (23.25, 77.41),
    "indore": (22.72, 75.86),
    "ashta": (23.02, 76.72)
}

def get_weather(city):
    city = city.lower()

    if city not in cities:
        print("City not available in database!")
        return

    latitude, longitude = cities[city]

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

    try:
        response = requests.get(url)
        data = response.json()

        if "current_weather" not in data:
            print("Weather data not found")
            return

        weather = data["current_weather"]

        print("\n====== Weather Report ======")
        print(f"City : {city.title()}")
        print(f"Temperature : {weather['temperature']} °C")
        print(f"Wind Speed : {weather['windspeed']} km/h")
        print(f"Time : {weather['time']}")
        print("============================")

    except Exception as e:
        print("Error:", e)


while True:
    city = input("\nEnter city (or exit): ")

    if city.lower() == "exit":
        break

    get_weather(city)