from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, Regexp, URL, AnyOf


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])

    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")]
    )

    photo_url = StringField("Photo URL", validators=[URL(), Optional()])

    age = IntegerField("Age", validators=[InputRequired(), AnyOf(
        [val for val in range(31)], message="Age must be between 0 and 30")])

    notes = TextAreaField("Comments", validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    notes = TextAreaField("Comments", validators=[Optional()])
    available = BooleanField("Avalaible")
