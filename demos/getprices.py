import requests
ip = "127.0.0.1"
port = 5000
def getprice(trade):
    r1 = requests.get("http://127.0.0.1:5000/gettprice?trade={}".format(trade))
    price = r1.json()
    return price
def getprices():

    


