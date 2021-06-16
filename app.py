from flask import Flask

app = Flask(__name__)
app.secret_key = '123'

# app.config.from_pyfile('settings.py')

from assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

from assignment11.assignment11 import assignment11
app.register_blueprint(assignment11)
if __name__ == '__main__':
    app.run(debug=True)
















