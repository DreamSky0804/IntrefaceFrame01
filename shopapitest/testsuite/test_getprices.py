import requests,json,pytest
from shopapitest.common.getcase import getdata
from configparser import ConfigParser
conf = ConfigParser()
conf.read("../configs/config.ini")
ip = conf.get("test","ip")
port = conf.get("test","port")
def getprice(trade):
    r1 = requests.get("http://127.0.0.1:5000/gettprice?trade={}".format(trade))
    price = r1.json()
    return price
datas = getdata()

@pytest.mark.parametrize("case,uri,param,exp",
                         datas,ids=[a[0] for a in datas])
def test_getprices(case,uri,param,exp):
    url = "http://{}:{}{}".format(ip, port, uri)
    print(url)
    param = json.loads(param)
    trade = param["trade"]
    price = getprice(trade)["data"]
    param["price"] = price
    urla = url + "?trade={trade}&price={price}&unit={unit}".format(**param)
    print(urla)
    r = requests.get(urla)
    print(r.json)
    assert r.status_code == 200, "status_code: {}".format(r.status_code)
    assert r.json()["data"] == str(exp), "price: {}".format(r.json()["data"])



