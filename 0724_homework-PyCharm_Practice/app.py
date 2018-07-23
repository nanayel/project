from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<path>')
def index(path=None):
    if path:
        return render_template('%s.html' % path)
    else:
        return render_template('base.html')


if __name__ == '__main__':
    app.run()


