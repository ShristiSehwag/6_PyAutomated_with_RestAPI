import requests

def get_weather(city, units='metrics',api_key='ad2e5822b8b019f5e96d8155d5ee38ff'):
  url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
  r = requests.get(url)
  content = r.json()

  with open('data.txt', 'a') as file:
    for dicty in content['list']:
      file.write(f"{dicty['dt_txt']},{dicty['main']['temp']},{dicty['weather'][0]['description']}"+'\n') 

