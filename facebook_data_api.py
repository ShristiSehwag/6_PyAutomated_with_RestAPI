import requests

url = '' # u'r cURL Value from fb developer account
def get_fb_response():
  response = requests.get(url)
  print(response.text)


