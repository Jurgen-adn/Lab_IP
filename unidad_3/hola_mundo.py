from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundito():
    return "<h1>¡Hola mundito desde flask!</h1>"
if __name__ == "__main__":
    app.run(debug=True)