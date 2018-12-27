import requests
from selenium import webdriver
def api(trade):
    body = {"trade": trade}
    # browser = webdriver.Chrome()
    r = requests.get("http://127.0.0.1:5000/gettprice?trade=%(trade)s"%body)
    price = r.json()
    body["price"] = price["data"]
    body["unit"] = 3
    print(body)
    r2 = requests.get("http://127.0.0.1:5000/getprices?trade=%(trade)s&price=%(price)s&unit=%(unit)d"%body)
    print(r2.text)

if __name__ == '__main__':
    trade = "banana"
    api(trade)