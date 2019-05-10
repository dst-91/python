from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":

    import logging
    logging.basicConfig(filename='debug.log',level=logging.DEBUG)
    logging.basicConfig(filename='error.log',level=logging.ERROR)

    app.run(host='0.0.0.0', port=5000, debug=True)
