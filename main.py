import requests

API_KEY = "70296315eea4e948ec06494ca51e9993"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()
    

    if data["cod"] != 200:
        print("❌ City not found. Please try again.")
        return

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    description = data["weather"][0]["description"]

    print(f"\nWeather in {city}")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind} m/s")


def main():
    while True:
        city = input("\nEnter city name: ")

        if city.lower() == "exit":
            print("Goodbye!")
            break

        get_weather(city)


if __name__ == "__main__":
    main()