from flask import Flask 


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "234assadf!12342@"
    
    return app

 