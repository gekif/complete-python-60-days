from flask import Flask, render_template, url_for

app = Flask("Website")


@app.route("/")
@app.route("/home")
def home():
    return render_template("tutorial.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)