from flask import Flask
from .home import HomeView
from .about import AboutView

def register_route(app: Flask):
    app.add_url_rule("/", view_func=HomeView.as_view("home"))
    app.add_url_rule("/about", view_func=AboutView.as_view("about"))

    