from flask import render_template
from flask.views import MethodView


class AboutView(MethodView):
    def get(self):
        return render_template("about.html", title="About")
    