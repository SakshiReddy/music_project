from flask import Flask, render_template 
from flask import request
app = Flask(__name__)


@app.route('/results')
def home():
    query=request.args.get("query")
    print(query)
    return str(query)


if __name__ == '__main__':
    app.run(debug=True, port=5001)

 