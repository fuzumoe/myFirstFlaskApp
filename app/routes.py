from flask import Flask, render_template


def register_route(app: Flask):
    
    # localhost:5000/ get
    @app.route("/")
    def home():
        return render_template("home.html", title="Home")
    
    # localhost:5000/about get
    @app.route("/about")
    def about():
        return render_template("about.html", title="About")