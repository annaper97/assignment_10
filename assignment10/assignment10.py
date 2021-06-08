from flask import Flask, render_template, Blueprint, request, redirect, flash
import mysql.connector



app = Flask(__name__)
app.secret_key = '123'

# app.config.fromm_pyfile('settings.py')
assignment10 = Blueprint('assignment10', __name__,
                static_folder='static',
                static_url_path='/assignment10',
                template_folder='templates')

@assignment10.route("/")
def home():
    return render_template('assignment10.html')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='assignment10')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@assignment10.route('/assignment10')
def index():
    query = "SELECT * FROM users"
    query_result = interact_db(query=query, query_type="fetch")
    return render_template('assignment10.html', users=query_result)


@assignment10.route('/insert_user', methods=['POST'])
def insert():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    query = "INSERT INTO users(first_name, last_name, email) VALUES ('%s','%s','%s')" % (first_name, last_name, email)
    interact_db(query=query, query_type="commit")
    flash('new user has been added')
    return redirect('assignment10')


@assignment10.route('/update_user', methods=['POST'])
def update():
    f_name = request.form['f_name']
    email = request.form['email']
    query = "UPDATE users SET first_name= '%s' WHERE email= '%s'" % (f_name,email)
    interact_db(query=query, query_type="commit")
    flash('user  details has been updated')
    return redirect('/assignment10')


@assignment10.route('/delete_user', methods=['POST'])
def delete():
    user_delete_by_email = request.form['email']
    query2 = "DELETE FROM users WHERE Email = '%s';" % user_delete_by_email
    interact_db(query=query2, query_type="commit")
    flash('user has been deleted')
    return redirect('/assignment10')


if __name__ == '__main__':
    app.run()
