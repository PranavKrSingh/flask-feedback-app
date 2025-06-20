from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Email

class FeedbackForm(FlaskForm):
    username = StringField("Name", validators=[DataRequired(message="It cannot be empty")])
    email = EmailField("Email", validators=[DataRequired(message="It cannot be empty"), Email(message="Input valid email")])
    message = StringField("Message", validators=[DataRequired(message="It cannot be empty")])
    submit = SubmitField("Submit Feedback")
