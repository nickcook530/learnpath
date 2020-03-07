from app_package import app
from app_package.models import Path, Step
from flask import redirect, url_for, flash, render_template
from flask_login import login_required, logout_user, current_user


@app.route('/')
def home():
    paths = []
    if current_user.is_authenticated:
        paths = Path.query.filter_by(user_id=current_user.id).all()
    return render_template("homescreen.html", paths=paths)

@app.route('/<user_id>/paths/<path_id>')
def path(user_id, path_id):
    path = Path.query.filter_by(user_id=user_id, id=path_id).first_or_404()
    steps = path.steps.all()
    return render_template("path.html", path=path, steps=steps)
    
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have logged out")
    return redirect(url_for("home"))