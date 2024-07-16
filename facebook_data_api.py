import requests

url = " " # u'r cURL Value from fb developer account
def get_fb_response():
  response = requests.get(url)
  print(response.text)

  # to fetch an image of account that you have access to 
  data = json.loads(data)
  image_url = data['images'][0]['source']
  image_bytes = requests.get(image_url).content

  with open('image.jpg', 'wb') as file:
    file.write(image_bytes)


