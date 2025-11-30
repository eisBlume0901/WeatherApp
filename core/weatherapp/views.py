from django.shortcuts import render
import requests
import environ

env = environ.Env()


def index(request):
    city = request.GET.get('city', 'Makati')
    api_key = env('OPENWEATHERMAP_API_KEY')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'

    weather_data = {}
    error_message = None

    try:
        response = requests.get(url).json()

        if response.get('cod') == 404:
            raise ValueError(f"'{city}' City not found. Please check the city name and try again.")

        weather_data = {
            'city': city,
            'temperature': response['main']['temp'],
            'humidity': response['main']['humidity'],
            'pressure': response['main']['pressure'],
            'description': response['weather'][0]['description'],
            'wind_speed': response['wind']['speed']
        }
    except ValueError as e:
        error_message = str(e)

    return render(request, 'index.html', {'weather_data': weather_data, 'error_message': error_message})
