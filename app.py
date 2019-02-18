from flask import flask

app = Flask(__name___)

@app.route('/')
def route():
    return 'INDEX'

if __name__ == '__main__':
    app.run()