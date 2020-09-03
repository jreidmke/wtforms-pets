from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, RadioField
from wtforms.validators import InputRequired, Optional, URL, AnyOf, NumberRange

class AddNewPetForm(FlaskForm):

    name = StringField('Pet Name')
    species = StringField('Pet Species', validators=[AnyOf(['cat', 'Cat', 'dog', 'Dog', 'fish', 'Fish'])])
    photo_url = StringField('Pet Image URL', validators=[URL(), Optional()])
    age = IntegerField('Pet Age', validators=[NumberRange(min=0, max=30)])
    notes = StringField('Pet Notes')
    available = RadioField(choices=[(1, "Available"), (0, 'Not Available')])