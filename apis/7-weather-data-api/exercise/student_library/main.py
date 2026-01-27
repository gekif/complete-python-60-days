from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)
df = pd.read_csv('dictionary.csv')


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/api/v1/<word>/')
def api(word):
    result = df.loc[df['word'] == word, 'definition']

    if result.empty:
        return {
            "error": "Sorry, we don't have this word in our dictionary."
        }, 404

    definition = result.iloc[0]

    return {
        'word': word.title(),
        'definition': definition
    }


if __name__ == "__main__":
    app.run(debug=True, port=5001)
