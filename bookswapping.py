from flask import Flask, render_template
from fakedata import cities

app = Flask(__name__)

@app.route('/')
@app.route('/cities')
def cityList():
    return render_template('cities.html', cities = cities)

@app.route('/cities/new')
def newCity():
    return "This page will allow to create a new city"

@app.route('/cities/<int:city_id>/edit')
def editCity(city_id):
    return "This page will allow to edit city %d" % city_id

@app.route('/cities/<int:city_id>/delete')
def deleteCity(city_id):
    return "This page will allow to delete city %d" % city_id

@app.route('/cities/<int:city_id>/books')
def bookList(city_id):
    return "This page will show all books for city %d" % city_id

@app.route('/cities/<int:city_id>/books/new')
def newBook(city_id):
    return "This page will allow to create a new book in city %d" % city_id

@app.route('/cities/<int:city_id>/books/<int:book_id>/edit')
def editBook(city_id, book_id):
    return "This page will allow to edit book %d in city %d" % (book_id, city_id)

@app.route('/cities/<int:city_id>/books/<int:book_id>/delete')
def deleteBook(city_id, book_id):
    return "This page will allow to delete book %d in city %d" % (book_id, city_id)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
