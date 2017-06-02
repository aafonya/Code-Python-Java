from flask import Flask
#from sqlalchemy import SQLAlchemy


app = Flask(__name__)
#db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return / hello_flask.html

if __name__ == '__main__':
    app.run()
