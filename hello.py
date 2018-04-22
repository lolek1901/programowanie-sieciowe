from flask import Flask
from flask import render_template
app = Flask(__name__)
import socket

@app.route("/")
def hello():
    return render_template('index.html',my_ip=get_ip(), moja_suma=31, moja_roznica=odejmowanie(), moj_iloczyn=iloczyn() )
	
def odejmowanie():
    a = 100
    b = 40
    return str(a-b)
	
def iloczyn():
    c=100
    d=30
    return str(c*d)
	
def get_ip():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    return ip_address
	 
@app.route("/test")
def test():
    return render_template('index.html', moja_suma=12)
	
@app.route("/suma")
def suma():
    a = 5
    b = 6
    return str(a+b)
	
@app.route("/iloczyn")
def iloczyn():
    a=5
    b=6
    return str(a*b)
	
if __name__ == '__main__':
    app.run()