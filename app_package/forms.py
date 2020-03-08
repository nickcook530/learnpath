from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length

class PathForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(max=5)])
    description = StringField('Description', validators=[InputRequired(), Length(max=4)])
    submit = SubmitField('Save')