from flask import Flask
app = Flask(__name__)

@app.route("/")
def Holaworld():
    return 'Hola World'

@app.route("/bye")
def Amigoworld():
    return 'Bye World'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug = True)