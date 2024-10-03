from api import fetch_weather_data

def get_data():
    while True:
        city_name = input("Enter the city name: ")
        weather_data = fetch_weather_data(city_name)
        if weather_data:  
            return weather_data
        else:
            print("Invalid location, please enter again.")
   
def print_weather_data(weather_data):
    if weather_data:
        detail = weather_data['current']['condition']['text']
        tempin_c = weather_data['current']['temp_c']
        humidity = weather_data['current']['humidity']
        wind_mph = weather_data['current']['wind_mph']
        
        print(f"Weather Condition : {detail}")
        print(f"Temperature       : {tempin_c} °C")
        print(f"Humidity          : {humidity} %")
        print(f"Wind speed        : {wind_mph} mph")
    else:
        print("Invalid location, please enter again.")

def main():
    weather_data = get_data()
    print_weather_data(weather_data)      
          
if __name__ == "__main__":
    main()
