<<<<<<< HEAD
from flask import Flask, render_template, request
from weather import main as get_weather

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        city = request.form['cityName']
        country = request.form['countryName']
        data = get_weather(city, country)
    return render_template('index.html', data=data)


if __name__ == '__main__':
=======
from flask import Flask, render_template, request
from weather import main as get_weather

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        city = request.form['cityName']
        country = request.form['countryName']
        data = get_weather(city, country)
    return render_template('index.html', data=data)


if __name__ == '__main__':
>>>>>>> d14245c66a1d1c1da78f162b6aa1d9526689fff7
    app.run(debug=True)