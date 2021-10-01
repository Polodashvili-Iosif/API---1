import requests

url_template = "http://wttr.in/{}?n?{}Tqu&lang={}"
location = "london"
url = url_template.format(location, 'u', 'en')

response = requests.get(url)
response.raise_for_status()

print(response.text)

location = "svo"
url = url_template.format(location, 'u', 'en')

response = requests.get(url)
response.raise_for_status()

print(response.text)
location = "Череповец"
url = url_template.format(location, 'm', 'ru')

response = requests.get(url)
response.raise_for_status()

print(response.text)