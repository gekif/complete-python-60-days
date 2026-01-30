from env import API_KEYS
import requests


def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?" \
        f"id={place}&" \
          f"&appid={API_KEYS}"

    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecast_days
    filtered_date = filtered_data[:nr_values]

    if kind == "Temperature":
        filtered_data = [dict['main']['temp'] for dict in filtered_date]

    if kind == "Sky":
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_date]

    return filtered_data

if __name__ == '__main__':
    print(get_data(place="Tokyo", forecast_days=3, kind="Temperature"))