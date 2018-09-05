import requests
response_obj = requests.get("https://www.youtube.com/feed/trending")
if response_obj.status_code == 200:
    print(response_obj.text)
