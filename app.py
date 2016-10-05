from flask import Flask,request,make_response
import re
app = Flask(__name__)

@app.route('/')
def index():
	lang = request.headers['Accept-Language'].split(',')[0]
	ip = request.remote_addr
	soft = re.search(r'(\([^)]+\))',request.headers['User-Agent']).group(0)[1:-1]
	resp = make_response(str({'ipaddress': ip, 'language': str(lang), 'software': str(soft)}))
	resp.headers['Content-Type'] = 'application/json'
	return resp
if __name__ == "__main__":
	app.run(host="0.0.0.0")