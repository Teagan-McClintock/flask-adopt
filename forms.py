"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Length, Optional, URL, AnyOf

class AddPetForm(FlaskForm):
    """Form for adding a pet to the agency"""

    name = StringField(
        "Pet Name",
        validators=[InputRequired(), Length(max=20)]
    )

    species = StringField("Species",
                        validators=[InputRequired(), AnyOf(['cat',
                                                        'porcupine',
                                                        'dog'])]
    )

    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()]
    )

    age = SelectField("Age", choices=[('baby', 'Baby'),
                                    ('young', 'Young'),
                                    ('adult', 'Adult'),
                                    ('senior', 'Senior')],
                                    validators=[InputRequired()]
    )
    notes = TextAreaField("Notes")