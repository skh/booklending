from flask import Flask, render_template, request, redirect, flash, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, City, Book

app = Flask(__name__)

engine = create_engine('sqlite:///bookswapping.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/cities')
def cityList():
    cities = session.query(City).all()
    return render_template('cities.html', cities = cities)

@app.route('/cities/new', methods=['GET','POST'])
def newCity():
    if request.method == 'POST':
        newCity = City(name = request.form['name'])
        session.add(newCity)
        session.commit()
        flash("New city %s was successfully added." % request.form['name'])
        return redirect(url_for('cityList'))
    else:
        return render_template('newcity.html')

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
    app.secret_key = "swapyourbooks!"
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
