import requests

url_params = {
    'amount': 10,
    'type': 'boolean',
}


url = f'https://opentdb.com/api.php?'
response = requests.get(url, params=url_params)
response.raise_for_status()
data = response.json()

question_data = data['results']  # 清單中裝著'字典型態的問題'
