import requests


url_template = "http://wttr.in/{}"
settings = {"london":  "en", "svo": "ru", "Череповец": "ru"}

for location in settings.keys():
    url = url_template.format(location)

    payload = {"n": "", "m": "", "T": "", "lang": settings[location]}

    response = requests.get(url, params=payload)
    response.raise_for_status()

    print(response.text)
