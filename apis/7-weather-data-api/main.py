from flask import Flask, render_template, url_for
import pandas as pd


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature =  df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10

    dict_station = {
        "date": date,
        "station": station,
        "temperature": temperature
    }

    return dict_station


if __name__ == "__main__":
    app.run(debug=True)