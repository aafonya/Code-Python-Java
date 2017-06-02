from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, session

app = Flask(__name__)
app.config.from_object(__name__)  # load config from this file , flaskr.py


@app.route('/', methods=['GET', 'POST'])
def root():
    return render_template('boards.html')

@app.route('/cards')
def cards():
    return render_template('cards.html')


if __name__ == '__main__':
    app.run(debug=True)

