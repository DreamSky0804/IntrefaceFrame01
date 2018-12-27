import requests
#获取单个产品的价钱
def apiprice(trade):
    r = requests.get("http://127.0.0.1:5000/gettprice?trade={}".format(trade))
    price = r.json()
    return price
#获取全部商品
def apigetall():
    r1 = requests.get("http://127.0.0.1:5000/gettrades")
    trades = r1.json()
    return trades
def apitest(trade,unit,exp):
    price = apiprice(trade)["data"]
    r2 = requests.get("http://127.0.0.1:5000/getprices?trade={}&price={}&unit={}".format(trade,price,unit))
    assert r2.status_code == 200,"status_code : {}".format(r2.status_code)
    prices = r2.json()["data"]
    assert str(exp) == prices,"prices is {}".format(prices)
    print(prices)
if __name__ == '__main__':
    exp = 4
    apitest("pear", "2", exp)



