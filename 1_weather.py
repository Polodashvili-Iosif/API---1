import requests


url_template = "http://wttr.in/{}"

settings = {
    "london":  "en",
    "svo": "ru",
    "Череповец": "ru",
}

for location, language in settings.items():
    url = url_template.format(location)

    payload = {
        "n": "",
        "m": "",
        "T": "",
        "q": "",
        "lang": language,
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()

    print(response.text)
