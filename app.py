from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/all_tutorials")
def all_tutorials():
	return render_template("all_tutorials.html")

@app.route("/examples")
def examples():
	return render_template("examples.html")


@app.route("/ursina")
def ursina():
	return render_template("ursina.html")

@app.route("/pygame")
def pygame():
	return render_template("pygame.html")


@app.route("/turtle")
def turtle():
	return render_template("turtle.html")


@app.route("/sqlite")
def sqlite():
	return render_template("sqlite.html")


@app.route("/tkinter")
def tkinter():
	return render_template("tkinter.html")


@app.route("/c")
def c():
	return render_template("c.html")


@app.route("/flask")
def flask():
	return render_template("flask.html")




if __name__ == "__main__":
	app.run(debug=True)
