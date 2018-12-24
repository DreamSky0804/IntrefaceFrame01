from flask import Flask, jsonify
from flask import render_template

app = Flask(__name__)
def getdata():
    trades = {}
    with open("trades.txt") as f:
        for line in f:
            line = line.strip()
            ts = line.split("|")
            trades[ts[0]] = round(float(ts[1]),2)
    return trades

def gettradedata():
    with open("trades.txt") as f:
        trades = f.readlines()
    return trades

def writetrades(trades):
    with open("trades.txt","w") as f:
        f.writelines(trades)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/gettrades",methods=["GET","POST"])
def gettrades():
    data = getdata()
    trades = data.keys()
    s = {"code":1000,"msg":"","trades":list(trades)}
    return jsonify(s)


if __name__ == '__main__':
    app.run()