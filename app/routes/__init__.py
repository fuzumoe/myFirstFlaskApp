from flask import Flask
from .home import HomeView
from .about import AboutView
from .contacts import ContactView

def register_route(app: Flask):
    app.add_url_rule("/", view_func=HomeView.as_view("home"))
    app.add_url_rule("/about", view_func=AboutView.as_view("about"))
    app.add_url_rule("/contacts", view_func=ContactView.as_view("contact"), methods=["GET", "POST"])

    