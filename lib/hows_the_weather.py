import random

def hows_the_weather():
    weather_options = ['sunny', 'rainy']
    weather = random.choice(weather_options)
    if weather == 'sunny':
        return 'Go out, its sunny'
    elif weather == 'rainy':
        return 'Stay home, its raining'