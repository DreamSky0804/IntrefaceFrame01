#获取全部商品
def gettrades():
    with open("trades.txt") as f:
        trades = f.readlines()
    return trades
#读取所有的商品
def writetrades(trades):
    with open("trades.txt","w") as f:
        f.writelines(trades)
#增加商品
def addtrade(trade,price):
    trades = gettrades()
    for t in trades:
        if trade in t:
            pass
    else:
        trades.append("{}|{}\n".format(trade,price))
        writetrades()
#删除商品
def deletetrade(trade):
    with open("trades.txt") as f:
        trades = f.readlines()
    for t in trades:
        if trade in t:
            trades.remove(t)
    with open("trades.txt","w") as f:
        f.writelines(trades)
#更新商品
def updatetrade(trade,price):
    with open("trades.txt") as f:
        trades = f.readlines()
    for t in trades:
        if trade in t:
            #利用了列表元素的可变性
            trades[trades.index(t)] = "{}|{}\n".format(trade,price)
    with open("trades.txt","w") as f:
        f.writelines(trades)
