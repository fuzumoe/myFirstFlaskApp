import logging 

from flask import redirect, render_template, flash, url_for
from flask.views import MethodView

from app.forms import ContactForm


logging.basicConfig(level=logging.ERROR)

logger =  logging.getLogger(__name__)


class ContactView(MethodView):
    def get(self):
        form = ContactForm()
        
        return render_template("contacts.html", title="Contact", form=form)
    
    def post(self):
        form = ContactForm()
        
        if form.validate_on_submit():
            flash(f"Message from {form.name.data} sent!")
            logger.info(form.name.data)
            return redirect(url_for("contact"))
        
        return render_template("contacts.html", title="Contact", form=form)