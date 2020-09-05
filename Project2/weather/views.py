import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm

def index(request):
    # YOUR_API_KEY = '7b18511d85c53711e518df9baa7666bf'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=7b18511d85c53711e518df9baa7666bf'
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7b18511d85c53711e518df9baa7666bf'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
        return redirect('/')

    form = CityForm()

    cities = City.objects.order_by('-id')

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()
        city_weather = {
            'id': city.id,
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/weather.html', context)


def deleteCity(request, pk):
    city = City.objects.get(id=pk)
    city.delete()
    return redirect('/')
