import requests



def get_news(topic, from_date, to_date, language='en',
            api_key='17fb352c8f7949a6922ed1c7833fb8aa'): 
  url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}8&sortBy=popularity&language={language}&apiKey={api_key}'
  r = requests.get(url)
  content = r.json()
  articles = content['articles']
  results = []
  for article in articles:
    print(f"\nTITLE\n{article['title']} \nDESCRIPTION:\n {article['description']}")
  

# NOTE: Change the from_date and to_date below to reflect recent dates
# Otherwise, you will get an error.


