from flask import Flask, render_template, Blueprint, request, redirect, flash ,jsonify
import mysql.connector, json

app = Flask(__name__)
app.secret_key = '123'

# app.config.fromm_pyfile('settings.py')
assignment11 = Blueprint('assignment11', __name__, static_folder='static',static_url_path='/assignment11.py',template_folder='templates')


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

@assignment11.route('/assignment11/users',methods=['GET'])
def usersList():
    query = "SELECT * FROM users"
    query_result = interact_db(query=query, query_type="fetch")
    response = query_result
    response =jsonify(response)
    return response

@assignment11.route('/assignment11/users/selected', defaults={'SOME_USER_ID': 1})
@assignment11.route('/assignment11/users/selected/<int:SOME_USER_ID>',methods=['GET'])
def usersID(SOME_USER_ID):
        query= "SELECT * FROM users WHERE id= '%s'" %(SOME_USER_ID)
        query_result = interact_db(query=query, query_type="fetch")
        response = {}
        if len(query_result) != 0:
            response =query_result[0]
        else:
            response =" The chosen user is not in the list"
        response = jsonify(response)
        return response


