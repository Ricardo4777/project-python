from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Mi First Deploy Galarza_Andy5"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8083)

