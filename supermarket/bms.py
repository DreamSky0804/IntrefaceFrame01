#!/usr/bin/env python
# coding=utf-8
#增加商品
def addtrade(trade,price):
    with open("trades.txt") as f:
        trades = f.readlines()
    for t in trades:
        if trade in t:
            pass
    else:
        trades.append("{}|{}\n".format(trade,price))
        with open("trades.txt","w") as f:
            f.writelines(trades)
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
if __name__ == '__main__':
    # addtrade("banana",3.5)
    # updatetrade("peach",12.5)
    deletetrade("banana")








