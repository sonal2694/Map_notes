from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.mapnotes

@app.route("/")
def main():
	return render_template('first_page.html')

@app.route("/login", methods=['POST'])
def login():
	username = request.form['username']
	password = request.form['password']
	loginDetails = db.loginDetails
	name = "Lozer"
	result = loginDetails.find_one({"username": username, "password": password})
	if result:
		name = result['name']
		return render_template('home_page.html', text=name)
	else:
		return render_template('first_page.html', text="Wrong Username/Password")

if __name__ == "__main__":
	app.run()