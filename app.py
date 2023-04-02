from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>First Flask App</h1>'

    

if __name__ == '__main__':
    app.run(debug = True, port=3000)