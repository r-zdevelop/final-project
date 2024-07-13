from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def weather():
    city = request.args.get('city')
    weather = get_current_weather(city)
    # City is not found by API
    if not weather['cod'] == 200:
        return render_template('city-not-found.html')
    
    return render_template(
        "weather.html", 
        title=weather['name'],
        status=weather['weather'][0]['description'].capitalize(),
        temp=f"{weather['main']['temp']:.1f}",
        feels_like=f"{weather['main']['feels_like']:.1f}"
    )

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8000)