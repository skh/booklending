Bookswapping

This is a web application that allows users to:

- login with Facebook or G+ accounts
- add cities to a database
- add books in a specific city to a database
- request a specific book from its current owner
- delete books from the database after giving them away

This web app can be run 
- locally with python
- locally with foreman (part of the heroku toolset)
- on Heroku


1. App Registration

This web application uses OAuth with Facebook and Google Plus for 
authentication, and needs to be registered with these OAuth providers.

Go to https://developers.facebook.com/ to register the app with your
Facebook account, and replace the information in fb_client_secrets.json
with your information.

Got to https://console.developers.google.com/ to register the app with
your Google account, and replace the file gp_client_secrets.json with the
client_secrets.json file provided by Google.

Be sure to set the URLs of your application correctly in your app's settings
at Google and Facebook. For local testing, you need to set it to 
http://localhost:5000/.

2. Database

Change the DATABASE_URL in the file database.py to the database you'd like
to use. The application will set up the database on first run.

The application is setup to be run against a Postgres database. If you want
to use a different database engine, you will need to install additional
dependencies in step 3.

See https://devcenter.heroku.com/articles/heroku-postgresql for information
on how to set up a Postgres database instance on Heroku. This can be used
for local testing as well.

3. Python dependencies

The dependencies of this application are listed in the file requirements.txt.

Heroku will set up the environment based on this file. For local deployment, run

  $ pip install -r requirements.txt

to install them all at once.

4. Local testing with plain python

Run

  $ python bookswapping.py

from the root directory of this application and point your browser at

	http://localhost:5000/

5. Local testing with foreman

If you have the Heroku tools installed, you can run the app with

	$ foreman start

from the root directory and point your browser at

	http://localhost:5000/

6. Deployment on Heroku

See

	https://devcenter.heroku.com/articles/getting-started-with-python#introduction

how to deploy python applications on Heroku.

Don't forget to change the allowed URLs of your application with the
OAuth provider tools for the OAuth login to be working from the
Heroku instance.
