from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/cities')
def cityList():
	return "This page will show all of my cities"

@app.route('/cities/new')
def newCity():
	return "This page will allow to create a new city"

@app.route('/cities/<int:city_id>/edit')
def editCity(city_id):
	return "This page will allow to edit city %d" % city_id

@app.route('/cities/<int:city_id>/delete')
def deleteCity(city_id):
	return "This page will allow to delete city %d" % city_id


if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)