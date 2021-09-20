from flask import Flask
from emoji import emojize
import clf


dc = {0: f"person name {emojize(':person:')}", 1: f"company name {emojize(':bank:')}"}

app = Flask(__name__)


@app.route('/<name>')
def pfpj(name):
    return f"{name} is a {dc[clf.clfpfpj.predict([name])[0]]}"


if __name__ == '__main__':
    app.run()
