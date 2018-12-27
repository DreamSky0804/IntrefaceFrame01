import requests,json
from shopapitest.common.getcase import getdata
ip = "127.0.0.1"
port = 5000
def getprice(trade):
    r1 = requests.get("http://127.0.0.1:5000/gettprice?trade={}".format(trade))
    price = r1.json()
    return price
def getprices(case,uri,param,exp):
    url = "http://{}:{}/".format(ip,port)
    param = json.loads(param)
    trade = param["trade"]
    price = getprice(trade)["data"]
    param["price"] = price
    url = url + "getprices?trade={trade}&price={price}&unit={unit}".format(**param)
    print(url)
    r = requests.get(url)
    print(r.json())
if __name__ == '__main__':
    datas = getdata()
    for case,uri,param,exp in datas:
        getprices(case,uri,param,exp )





    


