How to run this project:

- You'll need a reasonably recent Python version installed on your
computer (Flask states that it supports Python 3.5 and newer; I
used Python 3.8 while developing the project).

- (optional) Create a virtualenv in the project directory so that
you can keep your main Python environment free of unneeded packages

- Install Flask by using this terminal command: pip install Flask

- Set the FLASK_APP environment variable to the project.py file. On
Windows, the following command prompt command should be used:
C:[path to project directory]> set FLASK_APP=project.py

- Use the following terminal command to run the application on the
built-in test web server: python -m flask run

- Open the outputted URL (usually, it's http://127.0.0.1:5000/ ) in
the browser of your choice to start using the website.

For more information, check out the Installation and Quickstart
pages of the Flask documentation here:
https://flask.palletsprojects.com/en/1.1.x/installation/
https://flask.palletsprojects.com/en/1.1.x/quickstart/