from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "75a2bd3f0d171c23386cd9972055dc78"  # Your API key

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            weather_data = {"error": "City not found!"}
        else:
            weather_data = {
                "city": city,
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "icon": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}.png",
            }
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
