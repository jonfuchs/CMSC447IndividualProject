# CMSC 447, Individual Assignment
# By Jonathan Fuchs, Spring 2021

import sqlite3
from flask import Flask, render_template, g, request

app = Flask(__name__)

DATABASE = 'students.db'


# Helper function to access database
# Code copied from here: https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# Automatically close database when each route returns (from same source as above)
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# Homepage (static page)
@app.route('/')
def homepage():
    return render_template("homepage.html")


# View data page
@app.route('/view_data/')
def view_data():
    cur = get_db().cursor()
    cur.execute('SELECT * from student_info')
    column_names = cur.description
    row_list = cur.fetchall()
    return render_template("view_data.html", column_names=column_names, row_list=row_list)


# Update data page
@app.route('/update_data/', methods=['POST'])
def update_data():
    update_id = request.form['id']
    update_name = request.form['name']
    update_marks = request.form['marks']

    con = get_db()
    cur = con.cursor()
    cur.execute('SELECT * from student_info WHERE id=?', (update_id,))

    # If the select statement does not return any rows, there is no student
    # to update having the inputted id, so return an error page
    test = cur.fetchall()
    if len(test) == 0:
        return render_template("operation_result.html", status='id_not_found')

    cur.execute('UPDATE student_info SET name=?, marks=? WHERE id=?', (update_name, update_marks, update_id))
    con.commit()
    return render_template("operation_result.html", status='success')


# Add data page
@app.route('/add_data/', methods=['POST'])
def add_data():
    add_id = request.form['id']
    add_name = request.form['name']
    add_marks = request.form['marks']

    con = get_db()
    cur = con.cursor()
    cur.execute('SELECT * from student_info WHERE id=?', (add_id,))

    # If the select statement returns a nonempty list, there is already
    # a student who has the inputted id, so return an error page
    test = cur.fetchall()
    if len(test) != 0:
        return render_template("operation_result.html", status='id_exists')

    cur.execute('INSERT INTO student_info VALUES (?, ?, ?)', (add_id, add_name, add_marks))
    con.commit()
    return render_template("operation_result.html", status='success')


# Delete data page
@app.route('/delete_data/', methods=['POST'])
def delete_data():
    delete_id = request.form['id']

    con = get_db()
    cur = con.cursor()
    cur.execute('SELECT * from student_info WHERE id=?', (delete_id,))

    # If the select statement does not return any rows, there is no student
    # to delete having the inputted id, so return an error page
    test = cur.fetchall()
    if len(test) == 0:
        return render_template("operation_result.html", status='id_not_found')

    cur.execute('DELETE FROM student_info WHERE id=?', (delete_id,))
    con.commit()
    return render_template("operation_result.html", status='success')
