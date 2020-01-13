from flask import Flask, render_template 
from flask import request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method=="GET":

        return render_template('Music.html')
    else:

        query=request.form["query"]
        query = query.replace(" ", '+')
        print(query)
        URL = "http://127.0.0.1:5001/results?query="+ query
        r = requests.get(url = URL)
        print(r)
        return render_template('Music.html', url=URL)
        






if __name__ == '__main__':
    app.run(debug=True)
 