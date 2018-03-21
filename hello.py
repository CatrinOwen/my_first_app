from flask import Flask, render_template

app = Flask("MyApp")

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/idontexist")
def idontexist():
	return "I do exist now!"

@app.route("/catrin")
def name():
	return "hey"

app.run(debug=True)

# Flask to import the application
# app.route to define the route
# def for the methd name - to define
# return for what you want the browser to say