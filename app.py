from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/')
def index():
    return render_template('index.html', posts='test')
