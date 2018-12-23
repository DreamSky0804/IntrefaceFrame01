import time
#从文件获取商品,将读取到的商品与价格组成一个字典
def getdata():
         trades ={}
         with open("trades.txt") as f:
             for line in f:
                 line = line.strip()
                 ts = line.split("|")
                 #价格保留小数点后两位数字
                 trades[ts[0]] = round(float(ts[1]),2)
         return trades
#生成一个订单ID,并写入至文件中
def writedata(orderid):
    with open("ordersid.txt","a") as f:
        f.write(orderid+"\n")
#获取全部商品
def gettrades():
    data = getdata()
    trades = list(data.keys())
    return trades
#获取单一商品的价格
def getprice(trade):
    data = getdata()
    trades = gettrades()
    if trade in trades:
        return data.get(trade)
    return None
#获取所买商品的总价格
def getprices(trade,s,rate=1):
    price = getprice(trade)
    if price:
        pricenum = price*s*rate
        return pricenum
    return None
#生成订单ID
def createorderid(trade,s):
    prices = getprices(trade,s)
    #返回当前时间的时间戳（1970纪元后经过的浮点秒数）
    now = int(time.time())
    if prices:
        orderid = "%s%d%d"%(trade,prices*100,now)
        writedata(orderid)
        return orderid
    return 0

#购物
def goshopping():
    trades = gettrades()
    print("      \033[1;33;41m****welcome*****\033[0m")
    for t in trades:
        price = getprice(t)
        print("\033[1;31m%10s\033[0m:%10.2f" % (t, price))
    trade = input("\033[1;31mYou are going to buy that product:\n\033[0m")
    unit = input("\033[1;31mHow much do you plan to buy:\n\033[0m")
    prices = getprices(trade, int(unit))
    print("\033[1;31mYou need to pay:\033[0m   \033[1;33;41m%5.2f\033[0m" % prices)
    orderid = createorderid(trade, int(unit))
    print("\033[1;31mYour orderid is:%20s\n\033[0m" % orderid)
#逛街买东西
def main():
    flag = "Y"
    while flag == "Y":
        goshopping()
        flag = input("Do you want to continue buying? ")
        flag = flag[0].upper()
if __name__ == '__main__':
     main()












