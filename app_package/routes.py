from app_package import app
from flask import redirect, url_for, flash, render_template
from flask_login import login_required, logout_user


@app.route('/')
@app.route('/index')
def index():
    return render_template("base.html")
    
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have logged out")
    return redirect(url_for("index"))