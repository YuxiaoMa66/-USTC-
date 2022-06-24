import requests

url = "https://movie.douban.com/j/chart/top_list"

param = {
    'type': '11',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '100',
}

dic = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68'}

resp = requests.get(url = url, params = param, headers = dic)

print(resp.json())
resp.close()