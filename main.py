import weather_forecast as w
import get_news as n
import currency_api_own as c
import facebook_data_api as f

n.get_news(topic='space', from_date='2024-6-16', to_date='2024-6-16')

w.get_weather(city='Washington')

c.app.run(host='0.0.0.0')
# f.get_fb_response()