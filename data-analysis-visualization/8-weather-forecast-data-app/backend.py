from env import API_KEYS
import requests


def get_data(place, forecast_days=None, wind=None):
    url = f"http://api.weathermap.org/data/2.5/forecast?" \
        f"id={place}&" \
          f"&appid={API_KEYS}"

    response = requests.get(url)
    data = response.json()

    return data

if __name__ == '__main__':
    print(get_data(place="Tokyo"))