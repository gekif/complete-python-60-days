from flask import Flask, render_template, url_for
import pandas as pd


app = Flask(__name__)

stations = pd.read_csv("data/stations.txt", skiprows=17)
stations = stations[["STAID","STANAME                                 "]]

@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())

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

@app.route("/api/v1/<station>")
def all_data(station):
    filename = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    df['   TG'] = df['   TG'] / 10
    df = df.rename(columns={"    DATE": "date", "   TG": "temperature"})
    data = df.to_dict(orient="records")

    dict_station = {
        "station": station,
        "data": data
    }

    return dict_station


app.route("/api/v1/yearly/<station>/<year>")
def yearly_data(station, year):
    filename = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    df['   TG'] = df['   TG'] / 10
    df = df.rename(columns={"    DATE": "date", "   TG": "temperature"})
    df['year'] = df['date'].dt.year
    df_year = df[df['year'] == int(year)]
    data = df_year.drop(columns=['year']).to_dict(orient="records")

    dict_station = {
        "station": station,
        "year": year,
        "data": data
    }

    return dict_station

if __name__ == "__main__":
    app.run(debug=True)