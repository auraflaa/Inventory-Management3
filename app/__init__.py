from flask import Flask
from flask_mysqldb import MySQL
from flask import Blueprint

mysql = MySQL()

# Define blueprints for modular routes
main = Blueprint('main', __name__)

def create_app():
    app = Flask(__name__)

    # MySQL configuration
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'your_username'
    app.config['MYSQL_PASSWORD'] = 'your_password'
    app.config['MYSQL_DB'] = 'Inventory_Management'

    # Initialize MySQL
    mysql.init_app(app)

    # Register blueprints
    from .routes import main
    app.register_blueprint(main)

    return app