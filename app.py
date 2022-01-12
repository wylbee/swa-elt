from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker! Test 1.'

if __name__ == '__main__':
    app.run(port=5000)