from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length

class PathForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(max=120)])
    description = StringField('Description', validators=[InputRequired(), Length(max=400)])
    submit = SubmitField('Save')

class StepForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(max=120)])
    description = StringField('Description', validators=[InputRequired(), Length(max=400)])
    link = StringField('Link', validators=[Length(max=2048)])
    submit = SubmitField('Save')