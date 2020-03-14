from app_package import app, db
from app_package.models import Path, Step
from app_package.forms import PathForm, StepForm
from flask import redirect, url_for, flash, render_template
from flask_login import login_required, logout_user, current_user


@app.route('/', methods=['GET', 'POST'])
def home():
    path_form = PathForm()
    if path_form.validate_on_submit():
        new_path = Path(name=path_form.name.data, description=path_form.description.data, creator=current_user)
        db.session.add(new_path)
        db.session.commit()
        flash('SUCCESS')
        return redirect(url_for('path', user_id=current_user.id, path_id=new_path.id))
    paths = []
    if current_user.is_authenticated:
        paths = Path.query.filter_by(user_id=current_user.id).all()
    return render_template("homescreen.html", paths=paths, current_user=current_user, path_form=path_form)

@app.route('/<user_id>/paths/<path_id>', methods=['GET', 'POST'])
def path(user_id, path_id):
    path_form = PathForm() #consider removing this from base?
    step_form = StepForm()
    path = Path.query.filter_by(user_id=user_id, id=path_id).first_or_404()
    steps = path.steps.all()
    if step_form.validate_on_submit():
        new_step = Step(name=step_form.name.data, description=step_form.description.data, link=step_form.link.data, 
            path=path, creator=current_user)
        db.session.add(new_step)
        db.session.commit()
        flash('SUCCESS')
        return redirect(url_for('path', user_id=current_user.id, path_id=path.id))
    return render_template("path.html", path=path, steps=steps, creator_id=int(user_id), 
        current_user=current_user, path_form=path_form, step_form=step_form)
    
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have logged out")
    return redirect(url_for("home"))